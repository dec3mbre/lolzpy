from __future__ import annotations

import importlib

import pytest

collect_ignore_glob: list[str] = []

_CODEGEN_DEPS = ("jinja2", "prance", "datamodel_code_generator")

_missing = [d for d in _CODEGEN_DEPS if importlib.util.find_spec(d) is None]
if _missing:
    collect_ignore_glob.append("test_*.py")
