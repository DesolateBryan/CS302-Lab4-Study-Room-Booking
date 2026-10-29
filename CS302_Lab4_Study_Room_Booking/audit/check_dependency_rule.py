"""Audit every import in the entities and use_cases packages, including imports inside functions."""
import ast
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "study_room_booking"
INNER = (PACKAGE / "entities", PACKAGE / "use_cases")
COLUMNS = ("File", "Line", "Import", "Which circle does it name?", "Verdict")


def classify(module: str, file_layer: str):
    if module.startswith("study_room_booking.entities"):
        layer = "inner - entities"
        good = True
    elif module.startswith("study_room_booking.use_cases"):
        layer = "use cases"
        good = file_layer == "use_cases"
    elif module.startswith("study_room_booking.interface_adapters"):
        layer = "outer - interface adapters"
        good = False
    elif module.startswith("study_room_booking.frameworks_and_drivers"):
        layer = "outer - frameworks/drivers"
        good = False
    elif module.startswith("."):
        layer = "relative internal import (inspect manually)"
        good = False
    else:
        layer = "stable Python standard library" if module in {"dataclasses", "typing", "datetime", "collections", "abc"} else "unknown external import (review)"
        good = layer == "stable Python standard library"
    return layer, "inward / stable - OK" if good else "VIOLATION"


def scan():
    rows = []
    for layer_dir in INNER:
        for file in sorted(layer_dir.rglob("*.py")):
            for node in ast.walk(ast.parse(file.read_text())):
                if isinstance(node, ast.ImportFrom):
                    module = ("." * node.level + (node.module or ""))
                    expression = f"from {module} import {', '.join(x.name for x in node.names)}"
                elif isinstance(node, ast.Import):
                    module = node.names[0].name
                    expression = f"import {', '.join(x.name for x in node.names)}"
                else:
                    continue
                circle, verdict = classify(module, layer_dir.name)
                rows.append((str(file.relative_to(ROOT)), node.lineno, expression, circle, verdict))
    return sorted(rows, key=lambda row: (row[0], row[1]))


def main():
    rows = scan()
    print("DEPENDENCY AUDIT - all imports in the two inner layers")
    print(f"Total import statements: {len(rows)}; violations: {sum(row[4] == 'VIOLATION' for row in rows)}")
    for row in rows:
        print(f"{row[0]}:{row[1]} | {row[2]} | {row[3]} | {row[4]}")
    if "--csv" in sys.argv:
        with (ROOT / "audit" / "dependency_audit.csv").open("w", newline="") as output:
            writer = csv.writer(output)
            writer.writerow(COLUMNS)
            writer.writerows(rows)
    return 1 if any(row[4] == "VIOLATION" for row in rows) else 0


if __name__ == "__main__":
    raise SystemExit(main())
