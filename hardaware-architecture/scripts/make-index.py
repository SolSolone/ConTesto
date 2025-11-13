#!/usr/bin/env python3
"""Genera un semplice indice Markdown dei documenti principali."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
output = ["# Indice documentazione", ""]

sections = {
    "Requisiti": ROOT / "docs" / "requirements",
    "Use Cases": ROOT / "docs" / "usecases",
    "ADR": ROOT / "docs" / "adr",
}

for title, directory in sections.items():
    output.append(f"## {title}")
    for path in sorted(directory.glob("*.md")):
        if path.name.startswith("_"):
            continue
        rel = path.relative_to(ROOT)
        output.append(f"- [{path.stem}]({rel.as_posix()})")
    output.append("")

print("\n".join(output))
