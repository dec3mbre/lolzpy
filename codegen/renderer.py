"""Template rendering engine for code generation."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from codegen.parser import ParsedOperation, ParsedParameter, ParsedSpec

TEMPLATES_DIR = Path(__file__).parent / "templates"


# ---------------------------------------------------------------------------
# Template-friendly data wrappers
# ---------------------------------------------------------------------------

@dataclass(slots=True)
class TemplateOperation:
    """Operation data prepared for Jinja2 template rendering."""
    method_name: str
    http_method: str
    path: str
    path_template: str  # Path with Python f-string interpolation
    description: str | None
    path_params: list[ParsedParameter]
    query_params: list[ParsedParameter]
    body_params: list[ParsedParameter]
    required_query_params: list[ParsedParameter] = field(default_factory=list)
    optional_query_params: list[ParsedParameter] = field(default_factory=list)
    required_body_params: list[ParsedParameter] = field(default_factory=list)
    optional_body_params: list[ParsedParameter] = field(default_factory=list)
    is_multipart: bool = False
    file_params: list[ParsedParameter] = field(default_factory=list)
    form_params: list[ParsedParameter] = field(default_factory=list)
    response_model_name: str | None = None
    response_wrapper_key: str | None = None
    response_is_list: bool = False


def _prepare_operations(operations: list[ParsedOperation]) -> list[TemplateOperation]:
    """Convert parsed operations to template-friendly format."""
    result: list[TemplateOperation] = []
    for op in operations:
        # Convert path params like {item_id} to {item_id} for f-string
        path_params = op.path_params
        path_template = re.sub(
            r"\{(\w+)\}",
            lambda m, pp=path_params: f"{{{_param_python_name(m.group(1), pp)}}}",
            op.path,
        )

        required_query = [p for p in op.query_params if p.required]
        optional_query = [p for p in op.query_params if not p.required]
        required_body = [p for p in op.body_params if p.required]
        optional_body = [p for p in op.body_params if not p.required]
        file_params = [p for p in op.body_params if p.is_file]
        form_params = [p for p in op.body_params if not p.is_file]

        result.append(TemplateOperation(
            method_name=op.method_name,
            http_method=op.http_method,
            path=op.path,
            path_template=path_template,
            description=op.description,
            path_params=op.path_params,
            query_params=op.query_params,
            body_params=op.body_params,
            required_query_params=required_query,
            optional_query_params=optional_query,
            required_body_params=required_body,
            optional_body_params=optional_body,
            is_multipart=op.is_multipart,
            file_params=file_params,
            form_params=form_params,
            response_model_name=op.response_schema_name,
            response_wrapper_key=op.response_wrapper_key,
            response_is_list=op.response_is_list,
        ))
    return result


def _param_python_name(param_name: str, path_params: list[ParsedParameter]) -> str:
    """Find the python_name for a path parameter by its original name."""
    for p in path_params:
        if p.name == param_name:
            return p.python_name
    return param_name


# ---------------------------------------------------------------------------
# Jinja2 filters
# ---------------------------------------------------------------------------

def _pascal_filter(value: str) -> str:
    """Convert snake_case to PascalCase."""
    return "".join(word.capitalize() for word in value.split("_"))


def _truncate_filter(value: str, length: int = 200) -> str:
    """Truncate a string and append ... if needed."""
    if len(value) <= length:
        return value
    return value[:length - 3] + "..."


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def _create_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["pascal"] = _pascal_filter
    env.filters["truncate"] = _truncate_filter
    return env


def render_client(
    spec: ParsedSpec,
    package_name: str,
) -> str:
    """Render the client.py file from a parsed spec."""
    env = _create_env()
    template = env.get_template("client.py.jinja2")

    # Prepare template data
    groups: dict[str, list[TemplateOperation]] = {}
    for group_name, ops in spec.groups.items():
        groups[group_name] = _prepare_operations(ops)

    # Check if any operation uses Literal types
    has_literal = any(
        "Literal[" in p.python_type
        for ops in groups.values()
        for op in ops
        for p in op.query_params + op.body_params + op.path_params
    )

    # Collect model imports needed
    model_imports: set[str] = set()
    for ops in groups.values():
        for op in ops:
            if op.response_model_name:
                model_imports.add(op.response_model_name)

    return template.render(
        package_name=package_name,
        groups=groups,
        has_literal=has_literal,
        model_imports=sorted(model_imports),
    )


def render_init(
    spec: ParsedSpec,
    package_name: str,
    module_path: str,
) -> str:
    """Render the __init__.py file for a generated subpackage."""
    env = _create_env()
    template = env.get_template("init.py.jinja2")

    # Build sorted list of all Async*/Sync* class names
    class_names: list[str] = []
    for group_name in spec.groups:
        pascal = _pascal_filter(group_name)
        class_names.append(f"Async{pascal}")
        class_names.append(f"Sync{pascal}")
    class_names.sort()

    return template.render(
        package_name=package_name,
        module_path=module_path,
        class_names=class_names,
    )
