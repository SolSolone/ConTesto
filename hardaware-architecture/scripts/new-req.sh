#!/usr/bin/env bash
# Crea un nuovo requisito partendo dal template

set -euo pipefail

if [ $# -ne 1 ]; then
  echo "Uso: $0 REQ-XXX" >&2
  exit 1
fi

ID="$1"
TARGET_DIR="$(dirname "$0")/../docs/requirements"
TEMPLATE="$TARGET_DIR/_template.md"
OUTPUT="$TARGET_DIR/${ID}.md"

if [ -e "$OUTPUT" ]; then
  echo "Il file $OUTPUT esiste già" >&2
  exit 1
fi

sed "s/REQ-XXX/${ID}/g" "$TEMPLATE" > "$OUTPUT"
echo "Creato $OUTPUT"
