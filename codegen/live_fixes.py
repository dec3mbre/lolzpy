"""Post-generation live-fix patcher.

After datamodel-code-generator produces _models.py files, this module
applies known field overrides that make certain API fields Optional and
injects validators that are not expressible via the OpenAPI schema.

The patcher is idempotent -- running it on already-patched code produces
the same result.
"""

from __future__ import annotations

import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Per-field overrides: module -> list of (class, field, reason)
FIELD_OVERRIDES: dict[str, list[tuple[str, str, str]]] = {
    "forum": [
        ("Links2", "background_l", "not always present"),
        ("Links2", "background_m", "not always present"),
        ("Links2", "status", "not always present"),
        ("UserGroup", "user_group_icon_class", "not always present"),
        ("FieldModel", "is_multi_choice", "not always present"),
        ("FieldModel", "choices", "not always present"),
        ("FieldModel", "values", "not always present"),
        ("RespUserModel", "curator_titles", "not always present"),
        ("RespUserModel", "birthday", "can be null"),
    ],
    "market": [
        ("Rendered", "backgrounds", "can be non-dict"),
        ("UserModel", "age", "not always present"),
        ("UserModel", "balances", "not always present"),
        ("UserModel", "dob", "not always present"),
        ("UserModel", "feedback_data", "can be non-dict"),
        ("UserModel", "imap_data", "can be non-dict"),
        ("UserModel", "restore_data", "can be non-dict"),
        ("UserModel", "telegram_client", "can be non-dict"),
    ],
}

# Entire classes where ALL fields should be made Optional.
# Only a class-level comment is added; individual fields get no inline comment.
ALL_FIELDS_OPTIONAL: dict[str, list[tuple[str, str]]] = {
    "market": [
        ("CustomFields", "all custom fields are optional \u2014 not every user has every field"),
    ],
}

# Extra pydantic imports to ensure are present.
EXTRA_IMPORTS: dict[str, list[str]] = {
    "market": ["field_validator"],
}

# Validators to inject after a class's last field.
# module -> list of (class_name, code_block)
VALIDATORS: dict[str, list[tuple[str, str]]] = {
    "market": [
        (
            "Rendered",
            '    @field_validator("backgrounds", mode="before")\n'
            "    @classmethod\n"
            "    def _coerce_backgrounds(cls, v: Any) -> Any:\n"
            "        return v if isinstance(v, dict) else None\n",
        ),
        (
            "UserModel",
            '    @field_validator("feedback_data", "imap_data", "restore_data", "telegram_client", mode="before")\n'
            "    @classmethod\n"
            "    def _coerce_non_dict_to_none(cls, v: Any) -> Any:\n"
            "        return v if isinstance(v, dict) else None\n",
        ),
    ],
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

# Matches a single-line Annotated field:
#   field_name: Annotated[Type, Field(...)]
#   field_name: Annotated[Type, Field(...)] = default  # comment
_FIELD_RE = re.compile(
    r"^(?P<indent>\s+)"
    r"(?P<name>\w+):\s*Annotated\["
    r"(?P<type>[^,]+),\s*"
    r"(?P<field>Field\(.*?\))\]"
    r"(?P<default>.*)$",
)


def _make_optional(line: str, reason: str | None) -> str:
    """Make an Annotated field line Optional with ``= None``.

    If *reason* is a string, a ``# live-fix: <reason>`` comment is appended.
    If *reason* is None, no comment is added (used for whole-class overrides).
    The function is idempotent.
    """
    m = _FIELD_RE.match(line)
    if not m:
        return line

    indent = m.group("indent")
    name = m.group("name")
    raw_type = m.group("type").strip()
    field_part = m.group("field")

    suffix = f"  # live-fix: {reason}" if reason is not None else ""

    if "| None" in raw_type or "None |" in raw_type:
        # Type is already optional -- just ensure = None and comment
        return f"{indent}{name}: Annotated[{raw_type}, {field_part}] = None{suffix}"

    new_type = f"{raw_type} | None"
    return f"{indent}{name}: Annotated[{new_type}, {field_part}] = None{suffix}"


def _find_class_range(lines: list[str], class_name: str) -> tuple[int, int] | None:
    """Return ``(start, end)`` line indices for a class definition."""
    pattern = re.compile(rf"^class {re.escape(class_name)}\b")
    start = None
    for i, line in enumerate(lines):
        if pattern.match(line):
            start = i
            break
    if start is None:
        return None
    for i in range(start + 1, len(lines)):
        if re.match(r"^class \w+", lines[i]):
            return (start, i)
    return (start, len(lines))


def _fields_start(lines: list[str], start: int, end: int) -> int:
    """Index of the first field line after ``model_config``."""
    for i in range(start + 1, end):
        if lines[i].strip().startswith("model_config"):
            for j in range(i, end):
                if lines[j].strip() == ")":
                    return j + 1
            break
    return start + 1


def _last_field_index(lines: list[str], start: int, end: int) -> int:
    """Index of the last Annotated field line in a class body."""
    last = start
    for i in range(start, end):
        if _FIELD_RE.match(lines[i]):
            last = i
    return last


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def apply_live_fixes(models_path: str, module_name: str) -> int:
    """Apply live-fix patches to a generated ``_models.py`` file.

    Returns the number of modifications made.
    """
    path = Path(models_path)
    if not path.exists():
        return 0

    text = path.read_text()
    lines = text.splitlines()
    changes = 0

    # --- 1. Ensure extra imports -------------------------------------------
    for imp in EXTRA_IMPORTS.get(module_name, []):
        for i, line in enumerate(lines):
            if line.startswith("from pydantic import "):
                if imp not in line:
                    lines[i] = line.rstrip()
                    if lines[i].endswith(")"):
                        lines[i] = lines[i][:-1] + f", {imp})"
                    else:
                        lines[i] = lines[i] + f", {imp}"
                    changes += 1
                break

    # --- 2. Per-field overrides --------------------------------------------
    for class_name, field_name, reason in FIELD_OVERRIDES.get(module_name, []):
        cr = _find_class_range(lines, class_name)
        if cr is None:
            print(f"  Warning: class {class_name} not found for live-fix")
            continue
        start, end = cr
        field_pat = re.compile(rf"^\s+{re.escape(field_name)}:\s*Annotated\[")
        for i in range(start, end):
            if field_pat.match(lines[i]):
                new_line = _make_optional(lines[i], reason)
                if new_line != lines[i]:
                    lines[i] = new_line
                    changes += 1
                elif "# live-fix" not in lines[i]:
                    lines[i] = lines[i].rstrip() + f"  # live-fix: {reason}"
                    changes += 1
                break

    # --- 3. Whole-class optional overrides ---------------------------------
    for class_name, reason in ALL_FIELDS_OPTIONAL.get(module_name, []):
        cr = _find_class_range(lines, class_name)
        if cr is None:
            print(f"  Warning: class {class_name} not found for live-fix")
            continue
        start, end = cr
        fs = _fields_start(lines, start, end)

        # Insert class-level comment if missing
        comment_line = f"    # live-fix: {reason}"
        has_comment = any("# live-fix:" in lines[i] for i in range(start, end))
        if not has_comment:
            lines.insert(fs, comment_line)
            end += 1
            changes += 1

        # Make every Annotated field optional (no per-field comment)
        for i in range(fs, end):
            m = _FIELD_RE.match(lines[i])
            if m:
                new_line = _make_optional(lines[i], None)
                if new_line != lines[i]:
                    lines[i] = new_line
                    changes += 1

    # --- 4. Inject validators (process in reverse to avoid index shifts) ---
    for class_name, code_block in reversed(VALIDATORS.get(module_name, [])):
        # Idempotency: skip if the def is already present
        def_match = re.search(r"def (\w+)\(", code_block)
        if def_match and def_match.group(1) in "\n".join(lines):
            continue

        cr = _find_class_range(lines, class_name)
        if cr is None:
            print(f"  Warning: class {class_name} not found for validator injection")
            continue
        start, end = cr
        insert_at = _last_field_index(lines, start, end) + 1

        block_lines = [""] + code_block.splitlines()
        for j, bl in enumerate(block_lines):
            lines.insert(insert_at + j, bl)
        changes += 1

    if changes:
        path.write_text("\n".join(lines) + "\n")
        print(f"  Applied {changes} live-fix patch(es) to {models_path}")

    return changes
