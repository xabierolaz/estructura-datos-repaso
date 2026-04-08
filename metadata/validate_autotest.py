from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "autotest.ipynb"


def fail(message: str) -> None:
    raise SystemExit(message)


def main() -> None:
    if not NOTEBOOK.exists():
        fail("Falta autotest.ipynb")

    data = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    cells = data.get("cells", [])

    text_cells = ["".join(cell.get("source", [])) for cell in cells]
    joined = "\n".join(text_cells)

    for block in ["B01", "B02", "B03", "B04", "B05", "B06"]:
        if f"## {block} -" not in joined:
            fail(f"Falta la seccion {block}")
        if f"===== {block} =====" not in joined:
            fail(f"Falta el enlace de salida a entrega para {block}")

    spoiler_count = joined.count("<details>")
    if spoiler_count != 18:
        fail(f"Numero de spoilers incorrecto: {spoiler_count}")

    code_cells = [cell for cell in cells if cell.get("cell_type") == "code"]
    if len(code_cells) != 18:
        fail(f"Numero de celdas de compromiso incorrecto: {len(code_cells)}")

    if "Este cuaderno no es una entrega y no se corrige automaticamente." not in joined:
        fail("Falta la advertencia de que el cuaderno no es entrega")

    print("AUTOTEST OK")


if __name__ == "__main__":
    main()
