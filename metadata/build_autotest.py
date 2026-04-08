from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
TOPICS_PATH = ROOT / "metadata" / "autotest_topics.json"
OUTPUT_PATH = ROOT / "autotest.ipynb"

GITHUB_OWNER = "xabierolaz"
GITHUB_REPO = "estructura-datos-repaso"
GITHUB_BRANCH = "main"
GITHUB_WEB_BASE = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/blob/{GITHUB_BRANCH}"
COLAB_WEB_BASE = f"https://colab.research.google.com/github/{GITHUB_OWNER}/{GITHUB_REPO}/blob/{GITHUB_BRANCH}"


def md(text: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": dedent(text).strip("\n").splitlines(keepends=True),
    }


def code(text: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": dedent(text).strip("\n").splitlines(keepends=True),
    }


def github_url(path: str) -> str:
    return f"{GITHUB_WEB_BASE}/{path}"


def notebook(cells: list[dict]) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "colab": {
                "name": "Autotest diagnostico",
                "provenance": [],
                "toc_visible": True,
                "include_colab_link": False,
            },
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.12",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def intro_cells() -> list[dict]:
    colab_link = f"{COLAB_WEB_BASE}/autotest.ipynb"
    return [
        md(
            f"""
            # Autotest diagnostico

            [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_link})

            Flujo oficial del sistema:

            1. `autotest.ipynb`
            2. `resumen/`
            3. `entrega/entrega_spyder.py`

            Este cuaderno no es una entrega y no se corrige automaticamente.
            """
        ),
        md(
            """
            ## Como usar este cuaderno

            - antes de revelar una respuesta, escribe la tuya en la celda siguiente
            - marca honestamente si sale `sin_mirar`, `con_dudas` o `no_sale`
            - si un bloque sale flojo, vete a su `resumen/`
            - si un bloque sale limpio, pasa a `entrega/entrega_spyder.py`
            - este cuaderno diagnostica; no desarrolla la solucion completa
            """
        ),
    ]


def item_cells(topic: dict, item: dict, index: int) -> list[dict]:
    summary_url = github_url(topic["summary_path"].replace("../", ""))
    entrega_url = github_url("entrega/entrega_spyder.py")
    item_id = item["id"]
    placeholder = "Escribe aqui tu respuesta antes de abrir el spoiler."
    return [
        md(
            f"""
            ### {index}. {item["title"]}

            Tipo: `{item["type"]}`

            {item["prompt_html"]}

            Antes de abrir la solucion, escribe tu respuesta y tu estado en la siguiente celda.
            """
        ),
        code(
            f'''
            {item_id}_respuesta = """{placeholder}"""
            {item_id}_estado = "sin_mirar"  # cambia a: sin_mirar / con_dudas / no_sale

            assert {item_id}_respuesta.strip()
            assert {item_id}_respuesta.strip() != "{placeholder}"
            assert {item_id}_estado in {{"sin_mirar", "con_dudas", "no_sale"}}
            '''
        ),
        md(
            f"""
            <details>
            <summary>Ver respuesta esperada</summary>

            {item["expected_html"]}

            </details>

            Si aqui has marcado `con_dudas` o `no_sale`, vuelve al [resumen de {topic["block_id"]}]({summary_url}).
            Si sale limpio, luego podras pasar a la seccion `{topic["block_id"]}` de [entrega/entrega_spyder.py]({entrega_url}).
            """
        ),
    ]


def topic_cells(topic: dict) -> list[dict]:
    summary_url = github_url(topic["summary_path"].replace("../", ""))
    entrega_url = github_url("entrega/entrega_spyder.py")
    block = topic["block_id"]
    cells = [
        md(
            f"""
            ## {block} - {topic["name"]}

            Si este bloque no sale limpio, estudia [resumen {block}]({summary_url}).
            Si sale limpio, completa la seccion `{block}` en [entrega/entrega_spyder.py]({entrega_url}).
            """
        )
    ]
    for index, item in enumerate(topic["items"], 1):
        cells.extend(item_cells(topic, item, index))
    cells.append(
        md(
            f"""
            ### Salida del bloque {block}

            - si una o mas anclas han quedado en `con_dudas` o `no_sale`, estudia primero [resumen {block}]({summary_url})
            - si el bloque sale limpio, abre [entrega/entrega_spyder.py]({entrega_url}) y busca `===== {block} =====`
            - `python entrega/prueba.py --block {block}` es solo una comprobacion local opcional
            """
        )
    )
    return cells


def main() -> None:
    topics = json.loads(TOPICS_PATH.read_text(encoding="utf-8"))["topics"]
    cells: list[dict] = []
    cells.extend(intro_cells())
    for topic in topics:
        cells.extend(topic_cells(topic))
    cells.append(
        md(
            """
            ## Cierre

            El diagnostico solo vale si has sido honesto al marcar tus respuestas.
            Si un bloque no sale limpio, no pases directamente a la entrega.
            """
        )
    )
    OUTPUT_PATH.write_text(
        json.dumps(notebook(cells), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"rebuilt {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
