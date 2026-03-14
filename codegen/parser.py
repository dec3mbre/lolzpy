"""OpenAPI spec parser — converts an OpenAPI 3.x spec into an intermediate representation for code generation."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Intermediate representation
# ---------------------------------------------------------------------------

@dataclass(slots=True)
class ParsedParameter:
    """A single operation parameter (query, path, or body field)."""
    name: str
    python_name: str
    location: str  # "path", "query", "body"
    python_type: str
    required: bool
    default: str | None = None
    description: str | None = None
    enum_values: list[str] | None = None


@dataclass(slots=True)
class ParsedOperation:
    """A single API operation (e.g., GET /users)."""
    operation_id: str
    method_name: str
    http_method: str  # "GET", "POST", etc.
    path: str
    tags: list[str]
    description: str | None
    path_params: list[ParsedParameter]
    query_params: list[ParsedParameter]
    body_params: list[ParsedParameter]
    response_schema_name: str | None  # Name of the Pydantic model to return
    # For grouping into resource classes
    group: str  # Derived from first tag or operationId prefix


@dataclass(slots=True)
class ParsedSpec:
    """Fully parsed OpenAPI spec ready for code generation."""
    title: str
    base_url: str
    operations: list[ParsedOperation]
    groups: dict[str, list[ParsedOperation]] = field(default_factory=dict)

    def build_groups(self) -> None:
        self.groups.clear()
        for op in self.operations:
            self.groups.setdefault(op.group, []).append(op)


# ---------------------------------------------------------------------------
# Schema-type mapping
# ---------------------------------------------------------------------------

_TYPE_MAP: dict[str, str] = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "array": "list[Any]",
    "object": "dict[str, Any]",
}


def _schema_to_python_type(schema: dict[str, Any]) -> str:
    """Convert an OpenAPI schema to a Python type hint string."""
    if not schema:
        return "Any"

    # Handle nullable (OpenAPI 3.1 uses type as list)
    type_val = schema.get("type")
    if isinstance(type_val, list):
        types = [t for t in type_val if t != "null"]
        nullable = "null" in type_val
        base = _TYPE_MAP.get(types[0], "Any") if len(types) == 1 else "Any"
        return f"{base} | None" if nullable else base

    # Enum → Literal (only for small enums to avoid massive type annotations)
    enum = schema.get("enum")
    if enum and all(isinstance(v, str) for v in enum) and len(enum) <= 20:
        values = ", ".join(f'"{v}"' for v in enum)
        return f"Literal[{values}]"

    # $ref — shouldn't happen after resolution but handle gracefully
    if "$ref" in schema:
        ref = schema["$ref"]
        return ref.rsplit("/", 1)[-1]

    # Array
    if type_val == "array":
        items = schema.get("items", {})
        item_type = _schema_to_python_type(items)
        return f"list[{item_type}]"

    # oneOf / anyOf
    for key in ("oneOf", "anyOf"):
        variants = schema.get(key)
        if variants:
            types_list = [_schema_to_python_type(v) for v in variants]
            unique_types = list(dict.fromkeys(types_list))
            return " | ".join(unique_types) if len(unique_types) > 1 else unique_types[0]

    base = _TYPE_MAP.get(type_val or "", "Any")

    # Nullable
    if schema.get("nullable"):
        return f"{base} | None"

    return base


# ---------------------------------------------------------------------------
# Name helpers
# ---------------------------------------------------------------------------

_CAMEL_TO_SNAKE_RE1 = re.compile(r"([A-Z]+)([A-Z][a-z])")
_CAMEL_TO_SNAKE_RE2 = re.compile(r"([a-z0-9])([A-Z])")

def _to_snake_case(name: str) -> str:
    """Convert CamelCase/dot.notation to snake_case."""
    s = name.replace(".", "_").replace("-", "_").replace(" ", "_")
    s = _CAMEL_TO_SNAKE_RE1.sub(r"\1_\2", s)
    s = _CAMEL_TO_SNAKE_RE2.sub(r"\1_\2", s)
    return s.lower()


def _sanitize_python_name(name: str) -> str:
    """Make a string safe for use as a Python identifier."""
    s = _to_snake_case(name)
    s = re.sub(r"[^a-z0-9_]", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    if not s or s[0].isdigit():
        s = f"p_{s}"
    # Reserved words
    if s in ("class", "type", "from", "import", "return", "global", "lambda", "for", "in", "is", "not", "and", "or"):
        s = f"{s}_"
    return s


def _operation_id_to_method(operation_id: str) -> str:
    """Convert operationId like 'Threads.Create' to a method name like 'create'."""
    parts = operation_id.split(".")
    if len(parts) >= 2:
        return _sanitize_python_name(parts[-1])
    return _sanitize_python_name(operation_id)


def _operation_id_to_group(operation_id: str) -> str:
    """Extract group name from operationId like 'Threads.Create' → 'threads'."""
    parts = operation_id.split(".")
    if len(parts) >= 2:
        return _sanitize_python_name(parts[0])
    return "default"


# ---------------------------------------------------------------------------
# Ref resolution
# ---------------------------------------------------------------------------

def _resolve_ref(ref: str, spec: dict[str, Any]) -> dict[str, Any]:
    """Resolve a JSON $ref pointer within the spec."""
    if not ref.startswith("#/"):
        return {}
    parts = ref[2:].split("/")
    node: Any = spec
    for part in parts:
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(node, dict):
            node = node.get(part, {})
        else:
            return {}
    return node if isinstance(node, dict) else {}


def _resolve_schema(schema: dict[str, Any], spec: dict[str, Any]) -> dict[str, Any]:
    """Recursively resolve all $ref pointers in a schema."""
    if "$ref" in schema:
        schema = _resolve_ref(schema["$ref"], spec)

    # Resolve nested refs in array items
    if "items" in schema:
        schema = {**schema, "items": _resolve_schema(schema["items"], spec)}

    # Resolve nested refs in oneOf / anyOf / allOf
    for key in ("oneOf", "anyOf", "allOf"):
        if key in schema and isinstance(schema[key], list):
            schema = {**schema, key: [_resolve_schema(v, spec) for v in schema[key]]}

    # Resolve nested refs in properties
    if "properties" in schema and isinstance(schema["properties"], dict):
        schema = {
            **schema,
            "properties": {
                k: _resolve_schema(v, spec) for k, v in schema["properties"].items()
            },
        }

    return schema


# ---------------------------------------------------------------------------
# Parameter extraction
# ---------------------------------------------------------------------------

def _parse_parameter(param: dict[str, Any], spec: dict[str, Any]) -> ParsedParameter | None:
    """Parse a single OpenAPI parameter into a ParsedParameter."""
    # Resolve $ref
    if "$ref" in param:
        param = _resolve_ref(param["$ref"], spec)

    name = param.get("name")
    if not name:
        return None

    location = param.get("in", "query")
    schema = _resolve_schema(param.get("schema", {}), spec)
    python_type = _schema_to_python_type(schema)
    required = param.get("required", False)
    default = None

    if "default" in schema:
        default_val = schema["default"]
        if isinstance(default_val, str):
            default = f'"{default_val}"'
        elif isinstance(default_val, bool):
            default = str(default_val)
        elif default_val is None:
            default = "None"
        else:
            default = str(default_val)

    description = param.get("description")
    enum_values = schema.get("enum")

    return ParsedParameter(
        name=name,
        python_name=_sanitize_python_name(name),
        location=location,
        python_type=python_type,
        required=required,
        default=default,
        description=description,
        enum_values=enum_values,
    )


def _parse_request_body(request_body: dict[str, Any], spec: dict[str, Any]) -> list[ParsedParameter]:
    """Extract body parameters from a requestBody definition."""
    if "$ref" in request_body:
        request_body = _resolve_ref(request_body["$ref"], spec)

    params: list[ParsedParameter] = []
    content = request_body.get("content", {})

    # Prefer application/json
    json_content = content.get("application/json") or content.get("multipart/form-data")
    if not json_content:
        return params

    schema = _resolve_schema(json_content.get("schema", {}), spec)
    required_fields = set(schema.get("required", []))
    properties = schema.get("properties", {})

    for prop_name, prop_schema in properties.items():
        prop_schema = _resolve_schema(prop_schema, spec)
        python_type = _schema_to_python_type(prop_schema)
        is_required = prop_name in required_fields

        default = None
        if "default" in prop_schema:
            dv = prop_schema["default"]
            if isinstance(dv, str):
                default = f'"{dv}"'
            elif isinstance(dv, bool):
                default = str(dv)
            elif dv is None:
                default = "None"
            else:
                default = str(dv)

        params.append(ParsedParameter(
            name=prop_name,
            python_name=_sanitize_python_name(prop_name),
            location="body",
            python_type=python_type,
            required=is_required,
            default=default,
            description=prop_schema.get("description"),
            enum_values=prop_schema.get("enum"),
        ))

    return params


# ---------------------------------------------------------------------------
# Response schema name extraction
# ---------------------------------------------------------------------------

def _extract_response_schema_name(responses: dict[str, Any], spec: dict[str, Any]) -> str | None:
    """Extract the name of the response schema for the 200/201 response."""
    for code in ("200", "201", "2XX"):
        resp_def = responses.get(code, {})
        content = resp_def.get("content", {})
        json_content = content.get("application/json")
        if not json_content:
            continue
        schema = json_content.get("schema", {})
        if "$ref" in schema:
            return schema["$ref"].rsplit("/", 1)[-1]
        # Inline schema — return None, response will use dict[str, Any]
        return None
    return None


# ---------------------------------------------------------------------------
# Main parser
# ---------------------------------------------------------------------------

def parse_spec(spec_path: str | Path) -> ParsedSpec:
    """Parse an OpenAPI spec file into a ParsedSpec."""
    spec_path = Path(spec_path)
    with open(spec_path) as f:
        spec = json.load(f)

    title = spec.get("info", {}).get("title", spec_path.stem)
    servers = spec.get("servers", [])
    base_url = servers[0]["url"] if servers else ""

    operations: list[ParsedOperation] = []

    for path, path_item in spec.get("paths", {}).items():
        # Path-level parameters
        path_level_params = path_item.get("parameters", [])

        for http_method in ("get", "post", "put", "delete", "patch"):
            if http_method not in path_item:
                continue

            op = path_item[http_method]
            operation_id = op.get("operationId")
            if not operation_id:
                # Generate from method + path
                operation_id = f"{http_method}_{path.replace('/', '_').strip('_')}"

            tags = op.get("tags", [])
            description = op.get("summary") or op.get("description")

            # Merge path-level and operation-level parameters
            all_raw_params = path_level_params + op.get("parameters", [])

            path_params: list[ParsedParameter] = []
            query_params: list[ParsedParameter] = []

            seen_names: set[str] = set()
            for raw_param in all_raw_params:
                parsed = _parse_parameter(raw_param, spec)
                if parsed is None or parsed.name in seen_names:
                    continue
                seen_names.add(parsed.name)
                if parsed.location == "path":
                    parsed.required = True  # Path params are always required
                    path_params.append(parsed)
                elif parsed.location == "query":
                    query_params.append(parsed)
                # Skip header/cookie params

            # Request body
            body_params: list[ParsedParameter] = []
            request_body = op.get("requestBody")
            if request_body:
                body_params = _parse_request_body(request_body, spec)

            # Response schema
            response_schema_name = _extract_response_schema_name(
                op.get("responses", {}), spec
            )

            method_name = _operation_id_to_method(operation_id)
            group = _operation_id_to_group(operation_id)

            operations.append(ParsedOperation(
                operation_id=operation_id,
                method_name=method_name,
                http_method=http_method.upper(),
                path=path,
                tags=tags,
                description=description,
                path_params=path_params,
                query_params=query_params,
                body_params=body_params,
                response_schema_name=response_schema_name,
                group=group,
            ))

    parsed = ParsedSpec(title=title, base_url=base_url, operations=operations)
    # Deduplicate method names within groups
    parsed.build_groups()
    _deduplicate_method_names(parsed)
    return parsed


def _deduplicate_method_names(spec: ParsedSpec) -> None:
    """Ensure method names are unique within each group by appending a suffix."""
    for _group_name, ops in spec.groups.items():
        seen: dict[str, int] = {}
        for op in ops:
            if op.method_name in seen:
                seen[op.method_name] += 1
                # Append HTTP method for disambiguation
                op.method_name = f"{op.method_name}_{op.http_method.lower()}"
            else:
                seen[op.method_name] = 1
