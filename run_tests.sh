#!/usr/bin/env bash
set -euo pipefail

# script para ejecutar tests y generar reporte de cobertura
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

# crear venv si no existe
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# activar venv
# shellcheck disable=SC1091
source .venv/bin/activate

# instalar dependencias
pip install -r requirements.txt

# ejecutar pytest con cobertura y generar html
PYTHONPATH=. pytest --cov=src --cov-report=term-missing --cov-report=html "$@"

echo "Reporte de cobertura generado en htmlcov/index.html"
