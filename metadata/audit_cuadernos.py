from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "cuadernos"


@dataclass(frozen=True)
class BlockRule:
    folder: str
    min_cells: int
    required_phrases: tuple[str, ...]
    forbidden_phrases: tuple[str, ...]


RULES = (
    BlockRule(
        folder="01_fundamentos_python",
        min_cells=22,
        required_phrases=(
            "cero absoluto",
            "print` frente a `return",
            "Parametro frente a argumento",
            "enumerate",
            "desempaquetado",
            "Ruta absoluta",
            "Ruta relativa",
            "f-strings",
            "Type hints",
            "__name__",
            "docstring",
            "Comprobacion final",
        ),
        forbidden_phrases=("assert prediccion_",),
    ),
    BlockRule(
        folder="02_clases_y_objetos",
        min_cells=18,
        required_phrases=(
            "listas paralelas",
            "Clase frente a objeto",
            "__init__",
            "`self`",
            "Funcion frente a metodo",
            "diccionario",
            "Encapsulacion",
            "Invariantes",
            "CuentaBancaria",
            "Comprobacion final",
        ),
        forbidden_phrases=("assert prediccion_",),
    ),
    BlockRule(
        folder="03_stacks_y_queues",
        min_cells=18,
        required_phrases=(
            "ADT frente a implementacion",
            "List y map",
            "Stack",
            "Queue",
            "LIFO",
            "FIFO",
            "Stack frente a queue",
            "elige la estructura",
            "Comprobacion final",
        ),
        forbidden_phrases=("assert prediccion_",),
    ),
    BlockRule(
        folder="04_deque_priority_queue",
        min_cells=18,
        required_phrases=(
            "Deque",
            "double-ended queue",
            "appendleft",
            "popleft",
            "Priority queue",
            "Insercion ordenada",
            "Busqueda al extraer",
            "elige la estructura",
            "Comprobacion final",
        ),
        forbidden_phrases=("assert prediccion_",),
    ),
    BlockRule(
        folder="05_buffers_circulares",
        min_cells=18,
        required_phrases=(
            "Buffer frente a queue",
            "productor",
            "consumidor",
            "capacidad fija",
            "Politicas cuando se llena",
            "descartar el dato nuevo",
            "sobrescribir el dato mas antiguo",
            "bloquear",
            "% capacidad",
            "Comprobacion final",
        ),
        forbidden_phrases=("assert prediccion_",),
    ),
    BlockRule(
        folder="06_linked_lists",
        min_cells=28,
        required_phrases=(
            "Node",
            "head",
            "Como se recorre",
            "Linked list frente a lista Python",
            "`get` y `set`",
            "Insertar en cabeza",
            "Insertar en cola",
            "Insertar despues de un indice",
            "Borrar cabeza",
            "Borrar cola",
            "Borrar por valor",
            "Casos limite",
            "dunder",
            "Comprobacion final",
        ),
        forbidden_phrases=("assert prediccion_",),
    ),
)


def load_notebook(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["cells"]


def cell_text(cells: list[dict]) -> str:
    return "\n".join("".join(cell.get("source", [])) for cell in cells)


def grade_block(rule: BlockRule) -> tuple[int, list[str]]:
    path = NOTEBOOKS / rule.folder / "cuaderno.ipynb"
    issues: list[str] = []
    if not path.exists():
        return 0, [f"missing notebook: {path}"]

    cells = load_notebook(path)
    text = cell_text(cells)
    score = 0

    if len(cells) >= rule.min_cells:
        score += 2
    else:
        issues.append(f"expected at least {rule.min_cells} cells, found {len(cells)}")

    found = 0
    for phrase in rule.required_phrases:
        if phrase in text:
            found += 1
        else:
            issues.append(f"missing phrase: {phrase}")

    score += round(6 * found / len(rule.required_phrases))

    code_cells = [cell for cell in cells if cell["cell_type"] == "code"]
    markdown_cells = [cell for cell in cells if cell["cell_type"] == "markdown"]
    if len(code_cells) >= 6 and len(markdown_cells) >= 8:
        score += 1
    else:
        issues.append("expected richer mix of markdown and code cells")

    has_todo = "TODO" in text
    has_final = "Comprobacion final" in text
    if has_todo and has_final:
        score += 1
    else:
        issues.append("missing TODO work or final checkpoint")

    for phrase in rule.forbidden_phrases:
        if phrase in text:
            issues.append(f"forbidden phrase present: {phrase}")
            score = max(0, score - 2)

    return min(score, 10), issues


def main() -> None:
    total = 0
    max_total = len(RULES) * 10
    print("AUDITORIA DE CUADERNOS")
    print(f"root={ROOT}")
    print()
    for rule in RULES:
        score, issues = grade_block(rule)
        total += score
        print(f"{rule.folder}: {score}/10")
        if issues:
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("  - OK")
        print()
    print(f"TOTAL: {total}/{max_total}")


if __name__ == "__main__":
    main()
