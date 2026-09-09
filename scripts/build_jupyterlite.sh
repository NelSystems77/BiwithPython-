#!/usr/bin/env bash
# Regenera docs/lite/, la version ejecutable de los notebooks (JupyterLite +
# Pyodide) publicada en GitHub Pages. Correr desde la raiz del repositorio
# cada vez que cambien los notebooks o data/ventas.csv.
#
# Requiere:
#   pip install -r requirements-dev.txt

set -euo pipefail
cd "$(dirname "$0")/.."

STAGING_DIR="$(mktemp -d)"
trap 'rm -rf "$STAGING_DIR"' EXIT

mkdir -p "$STAGING_DIR/notebooks" "$STAGING_DIR/data"
cp notebooks/*.ipynb "$STAGING_DIR/notebooks/"
cp data/ventas.csv "$STAGING_DIR/data/ventas.csv"

rm -rf docs/lite
jupyter lite build \
  --contents "$STAGING_DIR" \
  --output-dir docs/lite \
  --apps notebooks --apps tree \
  --no-sourcemaps \
  --no-unused-shared-packages

rm -f .jupyterlite.doit.db

echo "Listo: docs/lite/ regenerado."
