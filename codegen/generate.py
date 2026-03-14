"""Code generation CLI — generates typed API clients from OpenAPI specs.

Usage:
    python -m codegen.generate --schema schemas/forum.json --name forum
    python -m codegen.generate --schema schemas/market.json --name market
    python -m codegen.generate --all
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from codegen.parser import parse_spec
from codegen.renderer import render_client, render_init

ROOT_DIR = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = Path(__file__).resolve().parent / "schemas"
SDK_DIR = ROOT_DIR / "lolz_sdk"

# Schema registry — add new schemas here
SCHEMAS: dict[str, dict[str, str]] = {
    "forum": {
        "schema": str(SCHEMAS_DIR / "forum.json"),
        "output_dir": str(SDK_DIR / "forum"),
        "module_path": "lolz_sdk.forum",
    },
    "market": {
        "schema": str(SCHEMAS_DIR / "market.json"),
        "output_dir": str(SDK_DIR / "market"),
        "module_path": "lolz_sdk.market",
    },
}


def generate_models(schema_path: str, output_path: str) -> None:
    """Run datamodel-code-generator to produce Pydantic v2 models."""
    cmd = [
        sys.executable, "-m", "datamodel_code_generator",
        "--input", schema_path,
        "--input-file-type", "openapi",
        "--output-model-type", "pydantic_v2.BaseModel",
        "--output", output_path,
        "--use-annotated",
        "--snake-case-field",
        "--allow-population-by-field-name",
        "--field-constraints",
        "--target-python-version", "3.11",
        "--collapse-root-models",
        "--use-standard-collections",
        "--use-union-operator",
    ]
    print("  Running datamodel-code-generator...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ERROR: datamodel-code-generator failed:\n{result.stderr}")
        sys.exit(1)
    print(f"  Models written to {output_path}")


def generate_client(schema_path: str, name: str, output_dir: str, module_path: str) -> None:
    """Parse the spec and render client + init files."""
    print("  Parsing OpenAPI spec...")
    spec = parse_spec(schema_path)
    print(f"  Found {len(spec.operations)} operations in {len(spec.groups)} groups")

    # Render client
    client_code = render_client(spec, name)
    client_path = Path(output_dir) / "_client.py"
    client_path.write_text(client_code)
    print(f"  Client written to {client_path}")

    # Render __init__.py
    init_code = render_init(spec, name, module_path)
    init_path = Path(output_dir) / "__init__.py"
    init_path.write_text(init_code)
    print(f"  Init written to {init_path}")


def format_output(output_dir: str) -> None:
    """Run ruff format on generated files."""
    cmd = [sys.executable, "-m", "ruff", "format", output_dir]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  Formatted {output_dir}")
    else:
        print(f"  Warning: ruff format failed: {result.stderr}")


def generate_one(name: str, config: dict[str, str]) -> None:
    """Generate models and client for a single API."""
    schema_path = config["schema"]
    output_dir = config["output_dir"]
    module_path = config["module_path"]

    print(f"\n{'='*60}")
    print(f"Generating: {name}")
    print(f"  Schema: {schema_path}")
    print(f"  Output: {output_dir}")
    print(f"{'='*60}")

    # Ensure output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Generate models
    models_path = str(Path(output_dir) / "_models.py")
    generate_models(schema_path, models_path)

    # Generate client
    generate_client(schema_path, name, output_dir, module_path)

    # Format
    format_output(output_dir)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate typed API clients from OpenAPI specs")
    parser.add_argument("--schema", help="Path to an OpenAPI JSON schema")
    parser.add_argument("--name", help="Name for the generated module (e.g., 'forum')")
    parser.add_argument("--all", action="store_true", help="Generate all registered schemas")
    args = parser.parse_args()

    if args.all:
        for name, config in SCHEMAS.items():
            generate_one(name, config)
    elif args.schema and args.name:
        config = {
            "schema": args.schema,
            "output_dir": str(SDK_DIR / args.name),
            "module_path": f"lolz_sdk.{args.name}",
        }
        generate_one(args.name, config)
    else:
        parser.error("Provide --all or both --schema and --name")

    print("\nDone!")


if __name__ == "__main__":
    main()
