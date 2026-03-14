"""Tests for the codegen pipeline — parser and renderer."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from codegen.parser import (
    ParsedSpec,
    _resolve_ref,
    _resolve_schema,
    _schema_to_python_type,
    parse_spec,
)
from codegen.renderer import render_client, render_init

# ---------------------------------------------------------------------------
# _schema_to_python_type
# ---------------------------------------------------------------------------


class TestSchemaToPythonType:
    def test_string(self):
        assert _schema_to_python_type({"type": "string"}) == "str"

    def test_integer(self):
        assert _schema_to_python_type({"type": "integer"}) == "int"

    def test_number(self):
        assert _schema_to_python_type({"type": "number"}) == "float"

    def test_boolean(self):
        assert _schema_to_python_type({"type": "boolean"}) == "bool"

    def test_array(self):
        assert _schema_to_python_type({"type": "array", "items": {"type": "string"}}) == "list[str]"

    def test_nested_array(self):
        schema = {"type": "array", "items": {"type": "array", "items": {"type": "integer"}}}
        assert _schema_to_python_type(schema) == "list[list[int]]"

    def test_empty_schema(self):
        assert _schema_to_python_type({}) == "Any"

    def test_nullable_type_list(self):
        result = _schema_to_python_type({"type": ["string", "null"]})
        assert result == "str | None"

    def test_small_enum_to_literal(self):
        schema = {"type": "string", "enum": ["a", "b", "c"]}
        result = _schema_to_python_type(schema)
        assert "Literal" in result
        assert '"a"' in result
        assert '"b"' in result

    def test_large_enum_falls_back(self):
        schema = {"type": "string", "enum": [f"v{i}" for i in range(25)]}
        result = _schema_to_python_type(schema)
        assert "Literal" not in result

    def test_unresolved_ref_fallback(self):
        result = _schema_to_python_type({"$ref": "#/components/schemas/Foo"})
        assert result == "Foo"

    def test_one_of(self):
        schema = {"oneOf": [{"type": "string"}, {"type": "integer"}]}
        result = _schema_to_python_type(schema)
        assert "str" in result
        assert "int" in result


# ---------------------------------------------------------------------------
# _resolve_ref / _resolve_schema
# ---------------------------------------------------------------------------


class TestResolveRef:
    def test_simple_ref(self):
        spec = {"components": {"schemas": {"Foo": {"type": "string"}}}}
        result = _resolve_ref("#/components/schemas/Foo", spec)
        assert result == {"type": "string"}

    def test_missing_ref(self):
        result = _resolve_ref("#/components/schemas/Missing", {})
        assert result == {}

    def test_non_hash_ref(self):
        result = _resolve_ref("external.json#/foo", {})
        assert result == {}


class TestResolveSchema:
    def test_resolves_direct_ref(self):
        spec = {"components": {"schemas": {"Bar": {"type": "integer"}}}}
        result = _resolve_schema({"$ref": "#/components/schemas/Bar"}, spec)
        assert result["type"] == "integer"

    def test_resolves_nested_array_items_ref(self):
        spec = {"components": {"schemas": {"ItemID": {"type": "integer"}}}}
        schema = {"type": "array", "items": {"$ref": "#/components/schemas/ItemID"}}
        result = _resolve_schema(schema, spec)
        assert result["items"]["type"] == "integer"
        assert "$ref" not in result["items"]

    def test_resolves_nested_oneof_refs(self):
        spec = {"components": {"schemas": {"A": {"type": "string"}, "B": {"type": "integer"}}}}
        schema = {"oneOf": [{"$ref": "#/components/schemas/A"}, {"$ref": "#/components/schemas/B"}]}
        result = _resolve_schema(schema, spec)
        assert result["oneOf"][0]["type"] == "string"
        assert result["oneOf"][1]["type"] == "integer"

    def test_passthrough_no_ref(self):
        schema = {"type": "string"}
        result = _resolve_schema(schema, {})
        assert result == {"type": "string"}


# ---------------------------------------------------------------------------
# parse_spec (integration)
# ---------------------------------------------------------------------------


class TestParseSpec:
    @pytest.fixture
    def mini_spec(self, tmp_path: Path) -> Path:
        spec = {
            "openapi": "3.1.0",
            "info": {"title": "Test", "version": "1.0"},
            "paths": {
                "/items": {
                    "get": {
                        "operationId": "Items.List",
                        "summary": "List items",
                        "tags": ["items"],
                        "parameters": [
                            {
                                "name": "limit",
                                "in": "query",
                                "schema": {"type": "integer"},
                            }
                        ],
                        "responses": {"200": {"description": "OK"}},
                    }
                },
                "/items/{item_id}": {
                    "get": {
                        "operationId": "Items.Get",
                        "summary": "Get one item",
                        "tags": ["items"],
                        "parameters": [
                            {
                                "name": "item_id",
                                "in": "path",
                                "required": True,
                                "schema": {"type": "integer"},
                            }
                        ],
                        "responses": {"200": {"description": "OK"}},
                    }
                },
            },
            "components": {"schemas": {}},
        }
        path = tmp_path / "spec.json"
        path.write_text(json.dumps(spec))
        return path

    def test_parse_operations(self, mini_spec: Path):
        result = parse_spec(str(mini_spec))
        assert isinstance(result, ParsedSpec)
        assert len(result.operations) == 2
        assert "items" in result.groups
        assert len(result.groups["items"]) == 2

    def test_path_params_detected(self, mini_spec: Path):
        result = parse_spec(str(mini_spec))
        get_item = [op for op in result.operations if op.method_name == "get"][0]
        assert len(get_item.path_params) == 1
        assert get_item.path_params[0].name == "item_id"

    def test_query_params_detected(self, mini_spec: Path):
        result = parse_spec(str(mini_spec))
        list_items = [op for op in result.operations if op.method_name == "list"][0]
        assert len(list_items.query_params) == 1
        assert list_items.query_params[0].name == "limit"


# ---------------------------------------------------------------------------
# render_client / render_init
# ---------------------------------------------------------------------------


class TestRenderer:
    @pytest.fixture
    def parsed_spec(self, tmp_path: Path) -> ParsedSpec:
        spec = {
            "openapi": "3.1.0",
            "info": {"title": "Test", "version": "1.0"},
            "paths": {
                "/items": {
                    "get": {
                        "operationId": "Items.List",
                        "summary": "List items",
                        "tags": ["items"],
                        "parameters": [],
                        "responses": {"200": {"description": "OK"}},
                    }
                },
            },
            "components": {"schemas": {}},
        }
        path = tmp_path / "spec.json"
        path.write_text(json.dumps(spec))
        return parse_spec(str(path))

    def test_render_client_contains_classes(self, parsed_spec: ParsedSpec):
        code = render_client(parsed_spec, "test_pkg")
        assert "class SyncItems:" in code
        assert "class AsyncItems:" in code
        assert "def list(" in code
        assert "async def list(" in code

    def test_render_init_contains_imports(self, parsed_spec: ParsedSpec):
        code = render_init(parsed_spec, "test_pkg", "test_pkg.api")
        assert "SyncItems" in code
        assert "AsyncItems" in code
