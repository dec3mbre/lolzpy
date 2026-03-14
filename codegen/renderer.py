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

    return template.render(
        package_name=package_name,
        groups=groups,
        has_literal=has_literal,
    )


def render_init(
    spec: ParsedSpec,
    package_name: str,
    module_path: str,
) -> str:
    """Render the __init__.py file for a generated subpackage."""
    env = _create_env()
    template = env.get_template("init.py.jinja2")
    return template.render(
        package_name=package_name,
        module_path=module_path,
        groups=list(spec.groups.keys()),
    )
