from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "cuadernos"
GITHUB_OWNER = "xabierolaz"
GITHUB_REPO = "estructura-datos-repaso"
GITHUB_BRANCH = "main"
REPO_SUBPATH = ""
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


def repo_path(path: str) -> str:
    return "/".join(part for part in (REPO_SUBPATH.strip("/"), path.strip("/")) if part)


def github_notebook_url(folder: str) -> str:
    return f"{GITHUB_WEB_BASE}/{repo_path(f'cuadernos/{folder}/cuaderno.ipynb')}"


def colab_notebook_url(folder: str) -> str:
    return f"{COLAB_WEB_BASE}/{repo_path(f'cuadernos/{folder}/cuaderno.ipynb')}"


def colab_badge(folder: str) -> dict:
    return md(
        f"""
        [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_notebook_url(folder)})

        [Ver este cuaderno en GitHub]({github_notebook_url(folder)})
        """
    )


def notebook(cells: list[dict], title: str) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "colab": {
                "name": title,
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


def write_notebook(folder: str, title: str, cells: list[dict]) -> None:
    path = NOTEBOOKS / folder / "cuaderno.ipynb"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(notebook(cells, title), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


COMMON_INTRO = """
## Como usar este cuaderno

- este cuaderno esta preparado para Google Colab
- no sustituye al `resumen/`; lo vuelve ejecutable
- en Colab usa el repo canonico de estudio, no tu repo individual de GitHub Classroom
- al ejecutarlo en Colab puedes clonar automaticamente el repo completo de estudio
- si vienes desde GitHub Classroom, la entrega real vive en `practica/**/ejercicios.py` de tu repo
- antes de correr una celda de prediccion, escribe tu respuesta en papel o en un comentario
- las celdas de prediccion ya no validan la respuesta correcta con `assert`; su trabajo es obligarte a comprometerte antes de ver el resultado
- al final haz siempre `Restart & Run All`
- despues del cuaderno vuelve a GitHub y resuelve `practica/` en `github.dev` o en local
- si pasas el cuaderno pero no puedes cerrar `ejercicios.py`, el bloque no esta dominado
"""


COLAB_INTRO = """
## Arranque en Google Colab

Flujo recomendado:

- abre este cuaderno en Google Colab
- este enlace de Colab abre el repo canonico de estudio
- ejecuta la celda siguiente para clonar `xabierolaz/estructura-datos-repaso`
- si quieres solo este cuaderno, puedes seguir sin clonar nada
- si quieres `resumen/` y `practica/` dentro de Colab, deja la clonacion activa
- esta sesion de Colab no entrega nada automaticamente a GitHub Classroom
"""


COLAB_BOOTSTRAP = """
from pathlib import Path
import os
import subprocess

IN_COLAB = "COLAB_RELEASE_TAG" in os.environ
PROJECT_ROOT = Path.cwd()

print("Entorno Colab:", IN_COLAB)
print("Directorio actual:", PROJECT_ROOT)
print("Aviso: esta sesion de Colab es para estudiar. La entrega real vive en tu repo de GitHub Classroom.")

REPO_URL = "https://github.com/xabierolaz/estructura-datos-repaso.git"
REPO_BRANCH = "main"
REPO_DIR = Path("/content/estructura_datos_repaso")
PROJECT_FOLDER = ""

if IN_COLAB and REPO_URL:
    if not REPO_DIR.exists():
        subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", REPO_BRANCH, REPO_URL, str(REPO_DIR)],
            check=True,
        )
    candidates = [
        REPO_DIR / PROJECT_FOLDER,
        REPO_DIR,
    ]
    project_candidate = next(
        (
            candidate
            for candidate in candidates
            if (candidate / "cuadernos").exists() and (candidate / "practica").exists()
        ),
        None,
    )
    if project_candidate is not None:
        os.chdir(project_candidate)
        PROJECT_ROOT = project_candidate
        print("Proyecto listo en:", PROJECT_ROOT)
    else:
        print("Repo clonado. Ajusta PROJECT_FOLDER o REPO_DIR si la carpeta del proyecto tiene otra forma.")
elif IN_COLAB:
    print("Modo Colab simple: puedes estudiar este cuaderno sin clonar nada.")
    print("Si quieres tambien resumen y practica, deja REPO_URL como esta y ejecuta de nuevo.")
else:
    print("Modo local: no hace falta configuracion extra.")
"""


def b01() -> list[dict]:
    return [
        md(
            """
            # B01 - Fundamentos de Python

            Resumen: [B01 teoria](../../resumen/01_fundamentos_python/README.md)  
            Transferencia: [B01 practica](../../practica/01_fundamentos_python/README.md)

            Objetivo del cuaderno:

            - arrancar desde cero absoluto en el uso basico del bloque
            - distinguir Parametro frente a argumento y `print` frente a `return`
            - recorrer listas con y sin indice
            - usar desempaquetado, Ruta absoluta, Ruta relativa, lectura de texto, `f-strings`, Type hints y `__name__`
            - salir listo para cerrar el bloque en Spyder
            """
        ),
        colab_badge("01_fundamentos_python"),
        md(COLAB_INTRO),
        code(COLAB_BOOTSTRAP),
        md(COMMON_INTRO),
        code(
            """
            from pathlib import Path
            import importlib
            """
        ),
        md(
            """
            ## Cero absoluto: como leer este bloque

            Si vienes de cero absoluto, la regla es esta:

            1. lee el enunciado de la celda
            2. predice en papel o en una variable de texto
            3. ejecuta
            4. explica con tus palabras que ha pasado
            """
        ),
        md(
            """
            ## Parametro frente a argumento

            Antes de ejecutar, escribe en papel:

            - cuales son los parametros
            - cuales son los argumentos
            - cuanto vale `resultado`
            """
        ),
        code(
            """
            tu_prediccion = "Escribe aqui lo que crees antes de seguir"
            assert tu_prediccion != "Escribe aqui lo que crees antes de seguir"
            """
        ),
        code(
            """
            def suma(a: int, b: int) -> int:
                return a + b


            resultado = suma(3, 5)
            print("resultado =", resultado)
            """
        ),
        md(
            """
            ## `print` frente a `return`

            Microtraza del bloque teorico:

            - `print` muestra
            - `return` devuelve
            - una funcion sin `return` explicito deja `None`
            """
        ),
        code(
            """
            def mal(x: int) -> None:
                print(x + 1)


            def bien(x: int) -> int:
                return x + 1


            valor_mal = mal(4)
            valor_bien = bien(4)
            print("valor_mal =", valor_mal)
            print("valor_bien =", valor_bien)
            assert valor_mal is None
            assert valor_bien == 5
            """
        ),
        md(
            """
            ## Listas, orden y recorrido

            Debes distinguir tres patrones:

            - solo necesito el valor
            - necesito indice y valor con `enumerate`
            - necesito controlar posiciones con `range(len(...))`
            """
        ),
        code(
            """
            values = ["a", "b", "c"]

            print("solo valor")
            for value in values:
                print(value)

            print("indice y valor")
            for index, value in enumerate(values):
                print(index, value)

            print("control de indices")
            for i in range(len(values)):
                print(i, values[i])
            """
        ),
        md(
            """
            ## Ejercicio guiado con `enumerate`

            Completa la funcion sin usar indices manuales.
            """
        ),
        code(
            """
            def etiquetar_con_indice(values: list[str]) -> list[str]:
                # TODO: usa enumerate y devuelve ['0:a', '1:b', ...]
                raise NotImplementedError("Completa etiquetar_con_indice")


            assert etiquetar_con_indice(["a", "b", "c"]) == ["0:a", "1:b", "2:c"]
            """
        ),
        md(
            """
            ## Desempaquetado

            Idea central:

            - Python reparte la estructura de la derecha sobre la forma de la izquierda
            - solo puede haber una variable con `*`
            """
        ),
        code(
            """
            first, *middle, last = [10, 20, 30, 40, 50]
            print(first, middle, last)
            assert first == 10
            assert middle == [20, 30, 40]
            assert last == 50
            """
        ),
        md(
            """
            ## Ruta absoluta frente a ruta relativa

            Tienes que ver ambas, no solo nombrarlas.
            """
        ),
        code(
            """
            data_dir = Path("tmp_b01")
            data_dir.mkdir(exist_ok=True)
            relative_path = data_dir / "numbers.txt"
            absolute_path = relative_path.resolve()
            relative_path.write_text("1 2 3\\n4 5\\n6 7\\n", encoding="utf-8")

            print("Ruta relativa:", relative_path)
            print("Ruta absoluta:", absolute_path)
            assert relative_path.exists()
            assert absolute_path.exists()
            """
        ),
        md(
            """
            ## Modos de apertura: `w` frente a `a`

            Antes de ejecutar, escribe que esperas en cada caso.
            """
        ),
        code(
            """
            modos_path = data_dir / "modos.txt"
            modos_path.write_text("hola\\n", encoding="utf-8")

            with open(modos_path, "w", encoding="utf-8") as f:
                f.write("x")
            despues_w = modos_path.read_text(encoding="utf-8")

            modos_path.write_text("hola\\n", encoding="utf-8")
            with open(modos_path, "a", encoding="utf-8") as f:
                f.write("x")
            despues_a = modos_path.read_text(encoding="utf-8")

            print("despues_w =", repr(despues_w))
            print("despues_a =", repr(despues_a))
            assert despues_w == "x"
            assert despues_a == "hola\\nx"
            """
        ),
        md(
            """
            ## Leer y transformar texto

            Completa la funcion usando `open`, `strip`, `split` e `int`.
            """
        ),
        code(
            """
            def cargar_numeros(path: str) -> list[int]:
                # TODO: usa open(...), strip(), split() e int(...)
                raise NotImplementedError("Completa cargar_numeros")


            assert cargar_numeros(str(relative_path)) == [1, 2, 3, 4, 5, 6, 7]
            """
        ),
        md(
            """
            ## `f-strings` y formato

            Recuerda: no son decoracion; son una forma controlada de construir texto.
            """
        ),
        code(
            """
            def formatear_media(nombre: str, media: float) -> str:
                # TODO: usa una f-string con 2 decimales
                raise NotImplementedError("Completa formatear_media")


            assert formatear_media("Ana", 7.5) == "Ana -> 7.50"
            assert formatear_media("Luis", 8) == "Luis -> 8.00"
            """
        ),
        md(
            """
            ## Type hints, comentario y docstring

            Este bloque no termina en saber escribir codigo que funciona. Tienes que saber leer una firma y documentar intencion.
            """
        ),
        code(
            """
            def get(matrix: list[list[int]], i: int, j: int) -> int:
                \"\"\"Devuelve el entero en la posicion i, j.\"\"\"
                # Este comentario explica una decision, no repite el codigo.
                return matrix[i][j]


            matrix = [[1, 2], [3, 4]]
            assert get(matrix, 1, 0) == 3
            print(get.__annotations__)
            print(get.__doc__)
            """
        ),
        md(
            """
            ## `__name__` y `main`

            En un notebook no trabajas igual que en un script, asi que vamos a simular un modulo real.
            """
        ),
        code(
            """
            module_path = data_dir / "mini_modulo.py"
            module_path.write_text(
                "print(__name__)\\n"
                "def main():\\n"
                "    return 'ok'\\n"
                "if __name__ == '__main__':\\n"
                "    print(main())\\n",
                encoding="utf-8",
            )

            mini_modulo = importlib.import_module("tmp_b01.mini_modulo")
            assert mini_modulo.main() == "ok"
            print("__name__ del notebook:", __name__)
            """
        ),
        md(
            """
            ## Comprobacion final

            No marques esta salida hasta que puedas contestar sin mirar:

            - que diferencia hay entre parametro y argumento
            - que diferencia real hay entre `print` y `return`
            - cuando usarias `enumerate`
            - que cambia entre `w` y `a`
            - por que una ruta relativa puede fallar
            - que hace `if __name__ == "__main__":`
            """
        ),
        code(
            """
            checklist_final = {
                "parametro_vs_argumento": False,
                "print_vs_return": False,
                "enumerate": False,
                "w_vs_a": False,
                "ruta_relativa": False,
                "__name__": False,
            }
            assert all(checklist_final.values()), "Cierra honestamente el checklist antes de salir del bloque."
            print("B01 listo para transferencia.")
            """
        ),
        md(
            """
            ## Cierre

            Cuando este cuaderno pase limpio con `Restart & Run All`, vuelve a tu repo de GitHub Classroom y cierra el bloque en [practica/01_fundamentos_python/ejercicios.py](../../practica/01_fundamentos_python/ejercicios.py). Si trabajas solo en navegador, usa `github.dev` con `.` y haz push para lanzar el autograding. Si trabajas en local, ejecuta despues `prueba.py`.
            """
        ),
    ]


def b02() -> list[dict]:
    return [
        md(
            """
            # B02 - Clases y objetos

            Resumen: [B02 teoria](../../resumen/02_clases_y_objetos/README.md)  
            Transferencia: [B02 practica](../../practica/02_clases_y_objetos/README.md)

            Objetivo del cuaderno:

            - pasar de listas paralelas a modelos con clase
            - distinguir Clase frente a objeto
            - entender `__init__`, `self`, atributo, metodo y Encapsulacion
            - practicar Invariantes antes de llegar a estructuras de datos
            """
        ),
        colab_badge("02_clases_y_objetos"),
        md(COLAB_INTRO),
        code(COLAB_BOOTSTRAP),
        md(COMMON_INTRO),
        md(
            """
            ## El problema: listas paralelas

            Antes de programar una estructura de datos, tienes que ver por que una clase mejora la representacion.
            """
        ),
        code(
            """
            nombres = ["Ana", "Luis"]
            edades = [20, 21]
            notas = [8.5, 6.0]

            print("listas paralelas -> el estudiante i queda repartido en tres estructuras")
            for i in range(len(nombres)):
                print(i, nombres[i], edades[i], notas[i])
            """
        ),
        md(
            """
            ## Clase frente a objeto

            Escribe en papel:

            - que es la clase
            - que es el objeto
            - donde viven los datos concretos
            """
        ),
        code(
            """
            respuesta_clase_objeto = "Escribe tu explicacion antes de seguir"
            assert respuesta_clase_objeto != "Escribe tu explicacion antes de seguir"
            """
        ),
        code(
            """
            class EstudianteDemo:
                def __init__(self, nombre, edad, nota):
                    self.nombre = nombre
                    self.edad = edad
                    self.nota = nota

                def es_aprobado(self):
                    return self.nota >= 5


            ana = EstudianteDemo("Ana", 20, 8.5)
            print(type(EstudianteDemo).__name__, type(ana).__name__)
            print(ana.nombre, ana.edad, ana.nota, ana.es_aprobado())
            """
        ),
        md(
            """
            ## `__init__`, `self`, atributos y metodos

            Regla del bloque:

            - `__init__` define como nace el objeto
            - `self` significa este objeto concreto
            - atributo = dato
            - metodo = comportamiento sobre ese estado
            """
        ),
        code(
            """
            class Counter:
                def __init__(self):
                    self.total = 0

                def add(self, value):
                    self.total += value


            c = Counter()
            c.add(3)
            c.add(7)
            assert c.total == 10
            """
        ),
        md(
            """
            ## Funcion frente a metodo

            Esto debe quedar limpio antes de seguir a `Stack` y `Queue`.
            """
        ),
        code(
            """
            def suma(a, b):
                return a + b


            class Caja:
                def __init__(self, valor):
                    self.valor = valor

                def duplicar(self):
                    self.valor *= 2


            caja = Caja(5)
            caja.duplicar()
            assert suma(2, 4) == 6
            assert caja.valor == 10
            """
        ),
        md(
            """
            ## Por que no basta un diccionario

            El diccionario puede guardar datos, pero no deja igual de claro el modelo ni protege reglas.
            """
        ),
        code(
            """
            estudiante_dict = {"nombre": "Ana", "edad": 20, "nota": 8.5}
            estudiante_dict["nota"] = "sobresaliente"
            print(estudiante_dict)
            """
        ),
        md(
            """
            ## Ejercicio guiado: clase `Estudiante`
            """
        ),
        code(
            """
            class Estudiante:
                def __init__(self, nombre: str, edad: int, nota: float):
                    # TODO: asigna atributos
                    raise NotImplementedError("Completa Estudiante.__init__")

                def es_aprobado(self) -> bool:
                    # TODO: devuelve True si nota >= 5
                    raise NotImplementedError("Completa Estudiante.es_aprobado")

                def resumen(self) -> str:
                    # TODO: texto tipo 'Ana (20) -> 8.50'
                    raise NotImplementedError("Completa Estudiante.resumen")


            estudiante = Estudiante("Ana", 20, 8.5)
            assert estudiante.nombre == "Ana"
            assert estudiante.edad == 20
            assert estudiante.nota == 8.5
            assert estudiante.es_aprobado() is True
            assert estudiante.resumen() == "Ana (20) -> 8.50"
            """
        ),
        md(
            """
            ## Encapsulacion

            En examen no basta con esconder datos; tienes que proteger reglas del modelo.
            """
        ),
        code(
            """
            class CuentaBancaria:
                def __init__(self, titular: str, saldo_inicial: float):
                    # TODO: guarda titular y __saldo
                    raise NotImplementedError("Completa CuentaBancaria.__init__")

                def depositar(self, cantidad: float) -> None:
                    # TODO: solo suma si cantidad > 0
                    raise NotImplementedError("Completa CuentaBancaria.depositar")

                def retirar(self, cantidad: float) -> bool:
                    # TODO: devuelve True si retira, False si no puede
                    raise NotImplementedError("Completa CuentaBancaria.retirar")

                def saldo(self) -> float:
                    # TODO
                    raise NotImplementedError("Completa CuentaBancaria.saldo")


            cuenta = CuentaBancaria("Ana", 100)
            assert cuenta.saldo() == 100
            cuenta.depositar(50)
            assert cuenta.saldo() == 150
            assert cuenta.retirar(20) is True
            assert cuenta.saldo() == 130
            assert cuenta.retirar(200) is False
            assert cuenta.saldo() == 130
            """
        ),
        md(
            """
            ## Invariantes

            Escribe con tus palabras que regla debe mantenerse siempre en `CuentaBancaria`.
            """
        ),
        code(
            """
            invariante = "Escribe la regla antes de seguir"
            assert invariante != "Escribe la regla antes de seguir"
            """
        ),
        md(
            """
            ## Comprobacion final

            No cierres el bloque si no puedes explicar:

            - por que una clase mejora frente a listas paralelas
            - Clase frente a objeto
            - que hace `__init__`
            - que significa `self`
            - Funcion frente a metodo
            - por que `__saldo` protege una regla y no solo un estilo
            """
        ),
        code(
            """
            checklist_final = {
                "listas_paralelas": False,
                "clase_objeto": False,
                "__init__": False,
                "self": False,
                "funcion_metodo": False,
                "encapsulacion": False,
            }
            assert all(checklist_final.values()), "Marca el checklist solo cuando de verdad lo puedas explicar."
            print("B02 listo para transferencia.")
            """
        ),
        md(
            """
            ## Cierre

            Cuando este cuaderno pase limpio con `Restart & Run All`, vuelve a tu repo de GitHub Classroom y cierra el bloque en [practica/02_clases_y_objetos/ejercicios.py](../../practica/02_clases_y_objetos/ejercicios.py). Si trabajas solo en navegador, usa `github.dev` con `.` y haz push para lanzar el autograding. Si trabajas en local, ejecuta despues `prueba.py`.
            """
        ),
    ]


def b03() -> list[dict]:
    return [
        md(
            """
            # B03 - ADT, stacks y queues

            Resumen: [B03 teoria](../../resumen/03_stacks_y_queues/README.md)  
            Transferencia: [B03 practica](../../practica/03_stacks_y_queues/README.md)

            Objetivo del cuaderno:

            - fijar ADT frente a implementacion
            - recordar List y map como ADT generales
            - razonar con LIFO y FIFO antes de programar
            - elegir la estructura correcta segun el problema
            """
        ),
        colab_badge("03_stacks_y_queues"),
        md(COLAB_INTRO),
        code(COLAB_BOOTSTRAP),
        md(COMMON_INTRO),
        md(
            """
            ## ADT frente a implementacion

            Punto central del bloque:

            - ADT = comportamiento y operaciones
            - implementacion = como lo representas por dentro
            """
        ),
        code(
            """
            respuesta_adt = "Escribe aqui un ejemplo de ADT y su implementacion"
            assert respuesta_adt != "Escribe aqui un ejemplo de ADT y su implementacion"
            """
        ),
        code(
            """
            stack_como_lista = [4, 9, 2]
            print("Representacion interna:", stack_como_lista)
            print("Comportamiento esperado: el ultimo en entrar sale primero")
            """
        ),
        md(
            """
            ## List y map como ADT generales

            No todo problema pide una Stack o una Queue.
            """
        ),
        code(
            """
            lista = ["Ana", "Luis", "Marta"]
            mapa = {"Ana": 8.5, "Luis": 6.0}

            assert lista[1] == "Luis"
            assert mapa["Ana"] == 8.5
            """
        ),
        md(
            """
            ## Stack

            Regla: LIFO.
            """
        ),
        code(
            """
            stack = []
            for value in [4, 9, 2]:
                stack.append(value)

            x = stack.pop()
            y = stack[-1]
            print("x =", x, "y =", y)
            assert x == 2
            assert y == 9
            """
        ),
        md(
            """
            ## Queue

            Regla: FIFO.
            """
        ),
        code(
            """
            queue = []
            for value in ["A", "B", "C"]:
                queue.append(value)

            x = queue.pop(0)
            y = queue[0]
            print("x =", x, "y =", y)
            assert x == "A"
            assert y == "B"
            """
        ),
        md(
            """
            ## Stack frente a queue

            Elige la estructura antes de implementarla.

            Regla corta para examen: elige la estructura segun el comportamiento, no segun el contenedor interno.
            """
        ),
        code(
            """
            escenarios = {
                "deshacer la ultima accion": "stack",
                "atender por orden de llegada": "queue",
                "cerrar parentesis pendientes": "stack",
                "procesar tareas segun entran": "queue",
            }
            print(escenarios)
            """
        ),
        md(
            """
            ## Ejercicio guiado: `Stack`
            """
        ),
        code(
            """
            class Stack:
                def __init__(self):
                    # TODO: usa una lista interna
                    raise NotImplementedError("Completa Stack.__init__")

                def push(self, item) -> None:
                    # TODO
                    raise NotImplementedError("Completa Stack.push")

                def pop(self):
                    # TODO
                    raise NotImplementedError("Completa Stack.pop")

                def peek(self):
                    # TODO
                    raise NotImplementedError("Completa Stack.peek")

                def is_empty(self) -> bool:
                    # TODO
                    raise NotImplementedError("Completa Stack.is_empty")

                def size(self) -> int:
                    # TODO
                    raise NotImplementedError("Completa Stack.size")


            s = Stack()
            assert s.is_empty() is True
            s.push(4)
            s.push(9)
            s.push(2)
            assert s.size() == 3
            assert s.peek() == 2
            assert s.pop() == 2
            assert s.peek() == 9
            assert s.size() == 2
            """
        ),
        md(
            """
            ## Ejercicio guiado: `Queue`
            """
        ),
        code(
            """
            class Queue:
                def __init__(self):
                    # TODO: usa una lista interna
                    raise NotImplementedError("Completa Queue.__init__")

                def enqueue(self, item) -> None:
                    # TODO
                    raise NotImplementedError("Completa Queue.enqueue")

                def dequeue(self):
                    # TODO
                    raise NotImplementedError("Completa Queue.dequeue")

                def peek(self):
                    # TODO
                    raise NotImplementedError("Completa Queue.peek")

                def is_empty(self) -> bool:
                    # TODO
                    raise NotImplementedError("Completa Queue.is_empty")

                def size(self) -> int:
                    # TODO
                    raise NotImplementedError("Completa Queue.size")


            q = Queue()
            assert q.is_empty() is True
            q.enqueue("A")
            q.enqueue("B")
            q.enqueue("C")
            assert q.size() == 3
            assert q.peek() == "A"
            assert q.dequeue() == "A"
            assert q.peek() == "B"
            assert q.size() == 2
            """
        ),
        md(
            """
            ## Comprobacion final

            No cierres el bloque hasta poder explicar:

            - ADT frente a implementacion
            - por que `list` y `map` no son lo mismo
            - LIFO y FIFO
            - por que una misma base interna puede dar dos comportamientos distintos
            - cuando elegir stack y cuando elegir queue
            """
        ),
        code(
            """
            checklist_final = {
                "adt": False,
                "list_map": False,
                "lifo_fifo": False,
                "misma_base_comportamiento_distinto": False,
                "elige_la_estructura": False,
            }
            assert all(checklist_final.values()), "Cierra honestamente el checklist antes de salir del bloque."
            print("B03 listo para transferencia.")
            """
        ),
        md(
            """
            ## Cierre

            Cuando este cuaderno pase limpio con `Restart & Run All`, vuelve a tu repo de GitHub Classroom y cierra el bloque en [practica/03_stacks_y_queues/ejercicios.py](../../practica/03_stacks_y_queues/ejercicios.py). Si trabajas solo en navegador, usa `github.dev` con `.` y haz push para lanzar el autograding. Si trabajas en local, ejecuta despues `prueba.py`.
            """
        ),
    ]


def b04() -> list[dict]:
    return [
        md(
            """
            # B04 - Deque y priority queue

            Resumen: [B04 teoria](../../resumen/04_deque_priority_queue/README.md)  
            Transferencia: [B04 practica](../../practica/04_deque_priority_queue/README.md)

            Objetivo del cuaderno:

            - entender por que `Deque` generaliza una queue
            - trabajar por ambos extremos
            - separar prioridad de antiguedad
            - comparar Insercion ordenada frente a Busqueda al extraer
            """
        ),
        colab_badge("04_deque_priority_queue"),
        md(COLAB_INTRO),
        code(COLAB_BOOTSTRAP),
        md(COMMON_INTRO),
        code(
            """
            from collections import deque
            """
        ),
        md(
            """
            ## Deque

            `Deque` significa `double-ended queue`.
            """
        ),
        code(
            """
            respuesta_deque = "Escribe con tus palabras que la diferencia de una queue normal"
            assert respuesta_deque != "Escribe con tus palabras que la diferencia de una queue normal"
            """
        ),
        code(
            """
            d = deque()
            d.append("b")
            d.appendleft("a")
            d.append("c")
            d.popleft()
            print(list(d))
            assert list(d) == ["b", "c"]
            """
        ),
        md(
            """
            ## Relacion con stack y queue

            Una `deque` puede comportarse como stack o como queue segun como la uses.
            """
        ),
        code(
            """
            d = deque()
            for value in [1, 2, 3]:
                d.append(value)
            como_stack = d.pop()

            d = deque()
            for value in [1, 2, 3]:
                d.append(value)
            como_queue = d.popleft()

            assert como_stack == 3
            assert como_queue == 1
            """
        ),
        md(
            """
            ## Ejercicio guiado: operaciones sobre `deque`
            """
        ),
        code(
            """
            def aplicar_operaciones_deque(operaciones: list[tuple[str, object]]) -> list[object]:
                # TODO: usa collections.deque y devuelve list(d)
                raise NotImplementedError("Completa aplicar_operaciones_deque")


            ops = [
                ("append", "b"),
                ("appendleft", "a"),
                ("append", "c"),
                ("popleft", None),
            ]
            assert aplicar_operaciones_deque(ops) == ["b", "c"]
            """
        ),
        md(
            """
            ## Priority queue

            Aqui manda la prioridad, no solo el orden de llegada.
            """
        ),
        code(
            """
            values = [3, 1, 5]
            print("si la prioridad mayor sale primero, el primer extraido deberia ser", max(values))
            """
        ),
        md(
            """
            ## Insercion ordenada frente a Busqueda al extraer

            Ambos caminos pueden dar la misma salida conceptual, pero pagan el coste en momentos distintos.
            """
        ),
        code(
            """
            def insertar_ordenado(items: list[int], value: int) -> list[int]:
                copia = items[:]
                copia.append(value)
                copia.sort()
                return copia


            def extraer_maximo_busqueda(items: list[int]) -> tuple[int, list[int]]:
                copia = items[:]
                mejor = max(copia)
                copia.remove(mejor)
                return mejor, copia


            ordenada = []
            for value in [3, 1, 5]:
                ordenada = insertar_ordenado(ordenada, value)
            extraido, resto = extraer_maximo_busqueda([3, 1, 5])

            assert ordenada == [1, 3, 5]
            assert extraido == 5
            assert resto == [3, 1]
            """
        ),
        md(
            """
            ## Ejercicio guiado: `PriorityQueueOrdenada`
            """
        ),
        code(
            """
            class PriorityQueueOrdenada:
                def __init__(self):
                    # TODO: usa una lista interna
                    raise NotImplementedError("Completa PriorityQueueOrdenada.__init__")

                def insertar(self, item: int) -> None:
                    # TODO: inserta manteniendo orden de menor a mayor
                    raise NotImplementedError("Completa PriorityQueueOrdenada.insertar")

                def extraer_maximo(self) -> int:
                    # TODO
                    raise NotImplementedError("Completa PriorityQueueOrdenada.extraer_maximo")

                def contenido(self) -> list[int]:
                    # TODO
                    raise NotImplementedError("Completa PriorityQueueOrdenada.contenido")


            pq = PriorityQueueOrdenada()
            for value in [3, 1, 5, 2]:
                pq.insertar(value)
            assert pq.contenido() == [1, 2, 3, 5]
            assert pq.extraer_maximo() == 5
            assert pq.extraer_maximo() == 3
            assert pq.contenido() == [1, 2]
            """
        ),
        md(
            """
            ## Elige la estructura

            - extremos -> deque
            - prioridad -> priority queue
            - regla de examen: elige la estructura por el criterio de salida
            """
        ),
        code(
            """
            elecciones = {
                "operar por izquierda y derecha": "deque",
                "sale antes lo mas urgente": "priority queue",
                "quiero LIFO estricto": "stack",
                "quiero FIFO estricto": "queue",
            }
            print(elecciones)
            """
        ),
        md(
            """
            ## Comprobacion final

            No cierres el bloque hasta poder explicar:

            - por que `Deque` generaliza una queue
            - que hacen `appendleft` y `popleft`
            - por que Priority queue no es una "cola por los dos lados"
            - Insercion ordenada frente a Busqueda al extraer
            - cuando elegir cada estructura
            """
        ),
        code(
            """
            checklist_final = {
                "deque_generaliza_queue": False,
                "appendleft_popleft": False,
                "priority_no_es_deque": False,
                "dos_enfoques_priority_queue": False,
                "elige_la_estructura": False,
            }
            assert all(checklist_final.values()), "Cierra honestamente el checklist antes de salir del bloque."
            print("B04 listo para transferencia.")
            """
        ),
        md(
            """
            ## Cierre

            Cuando este cuaderno pase limpio con `Restart & Run All`, vuelve a tu repo de GitHub Classroom y cierra el bloque en [practica/04_deque_priority_queue/ejercicios.py](../../practica/04_deque_priority_queue/ejercicios.py). Si trabajas solo en navegador, usa `github.dev` con `.` y haz push para lanzar el autograding. Si trabajas en local, ejecuta despues `prueba.py`.
            """
        ),
    ]


def b05() -> list[dict]:
    return [
        md(
            """
            # B05 - Buffers circulares

            Resumen: [B05 teoria](../../resumen/05_buffers_circulares/README.md)  
            Transferencia: [B05 practica](../../practica/05_buffers_circulares/README.md)

            Objetivo del cuaderno:

            - separar Buffer frente a queue
            - entender productor, consumidor y capacidad fija
            - comparar Politicas cuando se llena
            - implementar un buffer circular con sobrescritura
            """
        ),
        colab_badge("05_buffers_circulares"),
        md(COLAB_INTRO),
        code(COLAB_BOOTSTRAP),
        md(COMMON_INTRO),
        md(
            """
            ## Buffer frente a queue

            Recuerda:

            - queue = ADT y regla FIFO
            - buffer = almacenamiento temporal en un sistema
            """
        ),
        code(
            """
            definicion = "Escribe con tus palabras la diferencia entre Buffer frente a queue"
            assert definicion != "Escribe con tus palabras la diferencia entre Buffer frente a queue"
            """
        ),
        code(
            """
            sistema = {
                "productor": "genera mensajes",
                "consumidor": "procesa mensajes",
                "buffer": "absorbe desajustes temporales",
            }
            print(sistema)
            """
        ),
        md(
            """
            ## Capacidad fija

            Cuando hay capacidad fija, el problema ya no es solo FIFO.
            """
        ),
        code(
            """
            capacidad = 5
            indice = 4
            siguiente = (indice + 1) % capacidad
            print("si indice = 4 y capacidad = 5, siguiente =", siguiente)
            assert siguiente == 0
            """
        ),
        md(
            """
            ## Politicas cuando se llena

            Debes reconocer las tres:

            - descartar el dato nuevo
            - sobrescribir el dato mas antiguo
            - bloquear hasta que haya sitio
            """
        ),
        code(
            """
            def politica_descartar(buffer: list[int], capacidad: int, item: int) -> list[int]:
                return buffer[:] if len(buffer) >= capacidad else buffer + [item]


            def politica_sobrescribir(buffer: list[int], capacidad: int, item: int) -> list[int]:
                copia = buffer[:]
                if len(copia) >= capacidad:
                    copia.pop(0)
                copia.append(item)
                return copia


            print(politica_descartar([1, 2, 3], 3, 4))
            print(politica_sobrescribir([1, 2, 3], 3, 4))
            assert politica_descartar([1, 2, 3], 3, 4) == [1, 2, 3]
            assert politica_sobrescribir([1, 2, 3], 3, 4) == [2, 3, 4]
            """
        ),
        code(
            """
            def politica_bloquear(espacio_disponible: bool) -> str:
                return "inserta ahora" if espacio_disponible else "bloquear hasta que haya sitio"


            assert politica_bloquear(True) == "inserta ahora"
            assert politica_bloquear(False) == "bloquear hasta que haya sitio"
            """
        ),
        md(
            """
            ## Buffer circular

            La memoria da la vuelta, pero el orden logico sigue siendo FIFO sobre los datos activos.
            """
        ),
        code(
            """
            prediccion = "Escribe que contenido final esperas con capacidad 3 y entradas 1,2,3,4,5"
            assert prediccion != "Escribe que contenido final esperas con capacidad 3 y entradas 1,2,3,4,5"
            """
        ),
        code(
            """
            class BufferCircular:
                def __init__(self, capacidad: int):
                    # TODO: almacenamiento, indice de escritura y tamano actual
                    raise NotImplementedError("Completa BufferCircular.__init__")

                def push(self, item) -> None:
                    # TODO: sobrescribe el dato mas antiguo si esta lleno
                    raise NotImplementedError("Completa BufferCircular.push")

                def contenido(self) -> list:
                    # TODO: devuelve los elementos activos en orden FIFO
                    raise NotImplementedError("Completa BufferCircular.contenido")


            b = BufferCircular(3)
            b.push(1)
            b.push(2)
            assert b.contenido() == [1, 2]
            b.push(3)
            assert b.contenido() == [1, 2, 3]
            b.push(4)
            assert b.contenido() == [2, 3, 4]
            b.push(5)
            assert b.contenido() == [3, 4, 5]
            """
        ),
        md(
            """
            ## Cuando pensar en buffer y no en queue

            - streaming
            - productor/consumidor
            - capacidad fija
            - conservar solo lo reciente
            """
        ),
        code(
            """
            elecciones = {
                "orden de llegada sin mas restricciones": "queue",
                "almacenamiento temporal con capacidad fija": "buffer",
                "rafagas de datos y consumo desigual": "buffer",
            }
            print(elecciones)
            """
        ),
        md(
            """
            ## Mini decision de examen

            Si el foco es solo FIFO, piensa en queue.
            Si el foco es capacidad fija y politicas de llenado, piensa en buffer.
            """
        ),
        md(
            """
            ## Comprobacion final

            No cierres el bloque hasta poder explicar:

            - Buffer frente a queue
            - por que capacidad fija cambia el problema
            - las tres Politicas cuando se llena
            - por que `% capacidad` resuelve la vuelta al principio
            - cuando tiene sentido conservar solo los datos recientes
            """
        ),
        code(
            """
            checklist_final = {
                "buffer_vs_queue": False,
                "capacidad_fija": False,
                "politicas": False,
                "modulo": False,
                "datos_recientes": False,
            }
            assert all(checklist_final.values()), "Cierra honestamente el checklist antes de salir del bloque."
            print("B05 listo para transferencia.")
            """
        ),
        md(
            """
            ## Cierre

            Cuando este cuaderno pase limpio con `Restart & Run All`, vuelve a tu repo de GitHub Classroom y cierra el bloque en [practica/05_buffers_circulares/ejercicios.py](../../practica/05_buffers_circulares/ejercicios.py). Si trabajas solo en navegador, usa `github.dev` con `.` y haz push para lanzar el autograding. Si trabajas en local, ejecuta despues `prueba.py`.
            """
        ),
    ]


def b06() -> list[dict]:
    return [
        md(
            """
            # B06 - Linked lists

            Resumen: [B06 teoria](../../resumen/06_linked_lists/README.md)  
            Transferencia: [B06 practica](../../practica/06_linked_lists/README.md)

            Objetivo del cuaderno:

            - llegar desde clases y referencias hasta una linked list completa
            - entender `Node`, `head` y Como se recorre paso a paso
            - separar lectura, insercion, borrado y Casos limite
            - cerrar el bloque sin saltar directamente de cero a toda la clase final
            """
        ),
        colab_badge("06_linked_lists"),
        md(COLAB_INTRO),
        code(COLAB_BOOTSTRAP),
        md(COMMON_INTRO),
        md(
            """
            ## Punto de partida

            Para este bloque ya debes traer:

            - clases y objetos
            - atributos y metodos
            - bucles `while`
            - cuidado con `None`
            """
        ),
        md(
            """
            ## `Node`

            Una linked list es una secuencia de nodos. Cada `Node` guarda dato y referencia al siguiente.
            """
        ),
        code(
            """
            class Node:
                def __init__(self, data, next=None):
                    self.data = data
                    self.next = next


            n3 = Node(7)
            n2 = Node(4, n3)
            n1 = Node(9, n2)
            assert n1.data == 9
            assert n1.next.data == 4
            assert n1.next.next.data == 7
            """
        ),
        md(
            """
            ## `head`

            `head` es la puerta de entrada a toda la estructura.
            """
        ),
        code(
            """
            head = n1
            print("head apunta a:", head.data)
            assert head.next.next.data == 7
            """
        ),
        md(
            """
            ## Como se recorre

            Antes de ejecutar, escribe en papel en que nodo acabas.
            """
        ),
        code(
            """
            prediccion = "Escribe el dato final antes de ejecutar"
            assert prediccion != "Escribe el dato final antes de ejecutar"
            """
        ),
        code(
            """
            current = head
            current = current.next
            current = current.next
            print("current.data =", current.data)
            assert current.data == 7
            """
        ),
        md(
            """
            ## Linked list frente a lista Python

            - lista Python: acceso por indice natural
            - linked list: acceso por saltos desde `head`
            """
        ),
        code(
            """
            python_list = [9, 4, 7]
            assert python_list[2] == 7
            """
        ),
        md(
            """
            ## Operaciones de lectura

            Primero entrena recorrido con funciones sueltas antes de encapsularlo todo en la clase.
            """
        ),
        code(
            """
            def size_from_head(head: Node | None) -> int:
                total = 0
                current = head
                while current is not None:
                    total += 1
                    current = current.next
                return total


            def contains_from_head(head: Node | None, item) -> bool:
                current = head
                while current is not None:
                    if current.data == item:
                        return True
                    current = current.next
                return False


            assert size_from_head(head) == 3
            assert contains_from_head(head, 4) is True
            assert contains_from_head(head, 8) is False
            """
        ),
        md(
            """
            ## `get` y `set`

            En una linked list el indice no da acceso directo; representa saltos desde `head`.
            """
        ),
        code(
            """
            def get_from_head(head: Node | None, index: int):
                current = head
                current_index = 0
                while current is not None and current_index < index:
                    current = current.next
                    current_index += 1
                return None if current is None else current.data


            def set_from_head(head: Node | None, index: int, value) -> bool:
                current = head
                current_index = 0
                while current is not None and current_index < index:
                    current = current.next
                    current_index += 1
                if current is None:
                    return False
                current.data = value
                return True


            assert get_from_head(head, 0) == 9
            assert get_from_head(head, 2) == 7
            assert set_from_head(head, 1, 40) is True
            assert get_from_head(head, 1) == 40
            assert set_from_head(head, 7, 99) is False
            head.next.data = 4
            """
        ),
        md(
            """
            ## Insertar en cabeza
            """
        ),
        code(
            """
            def add_head_raw(head: Node | None, item) -> Node:
                return Node(item, head)


            head2 = add_head_raw(head, 2)
            assert size_from_head(head2) == 4
            assert head2.data == 2
            assert head2.next.data == 9
            """
        ),
        md(
            """
            ## Insertar en cola
            """
        ),
        code(
            """
            def add_tail_raw(head: Node | None, item) -> Node:
                if head is None:
                    return Node(item)
                current = head
                while current.next is not None:
                    current = current.next
                current.next = Node(item)
                return head


            solo = None
            solo = add_tail_raw(solo, 4)
            solo = add_tail_raw(solo, 7)
            assert size_from_head(solo) == 2
            assert solo.next.data == 7
            """
        ),
        md(
            """
            ## Insertar despues de un indice

            La clave es no perder el resto de la cadena al tocar `next`.
            """
        ),
        code(
            """
            def add_after_index_raw(head: Node | None, index: int, item) -> bool:
                current = head
                current_index = 0
                while current is not None and current_index < index:
                    current = current.next
                    current_index += 1
                if current is None:
                    return False
                current.next = Node(item, current.next)
                return True


            middle = Node("A", Node("B", Node("C")))
            assert add_after_index_raw(middle, 1, "X") is True
            assert get_from_head(middle, 0) == "A"
            assert get_from_head(middle, 1) == "B"
            assert get_from_head(middle, 2) == "X"
            assert get_from_head(middle, 3) == "C"
            assert add_after_index_raw(middle, 10, "Y") is False
            """
        ),
        md(
            """
            ## Borrar cabeza
            """
        ),
        code(
            """
            def remove_head_raw(head: Node | None):
                if head is None:
                    return None, None
                return head.data, head.next


            borrado, resto = remove_head_raw(head2)
            assert borrado == 2
            assert resto.data == 9
            """
        ),
        md(
            """
            ## Borrar cola

            Aqui necesitas el penultimo nodo, no solo el ultimo.
            """
        ),
        code(
            """
            def remove_tail_raw(head: Node | None):
                if head is None:
                    return None, None
                if head.next is None:
                    return head.data, None

                current = head
                while current.next.next is not None:
                    current = current.next

                removed = current.next.data
                current.next = None
                return removed, head


            removed, reduced = remove_tail_raw(add_tail_raw(add_head_raw(None, 4), 7))
            assert removed == 7
            assert reduced.data == 4
            assert reduced.next is None
            """
        ),
        md(
            """
            ## Borrar por valor

            Si borras un nodo del medio, el trabajo real es reconectar bien anterior y siguiente.
            """
        ),
        code(
            """
            def remove_by_value_raw(head: Node | None, item):
                if head is None:
                    return None, None
                if head.data == item:
                    return item, head.next

                previous = head
                current = head.next
                while current is not None:
                    if current.data == item:
                        previous.next = current.next
                        return item, head
                    previous = current
                    current = current.next
                return None, head


            chain = Node("A", Node("B", Node("C")))
            removed, chain = remove_by_value_raw(chain, "B")
            assert removed == "B"
            assert get_from_head(chain, 0) == "A"
            assert get_from_head(chain, 1) == "C"
            removed, chain = remove_by_value_raw(chain, "Z")
            assert removed is None
            """
        ),
        md(
            """
            ## Casos limite

            Este bloque exige pensar siempre en:

            - lista vacia
            - lista de un elemento
            - perder la cadena por tocar `next` demasiado pronto
            """
        ),
        code(
            """
            assert remove_head_raw(None) == (None, None)
            assert remove_tail_raw(None) == (None, None)
            unico = Node(5)
            assert remove_tail_raw(unico) == (5, None)
            """
        ),
        md(
            """
            ## LinkedList completa

            Ahora si: encapsula todo lo anterior dentro de la clase del bloque.
            """
        ),
        code(
            """
            class LinkedList:
                def __init__(self):
                    # TODO: guarda la cabeza
                    raise NotImplementedError("Completa LinkedList.__init__")

                def add_head(self, item) -> None:
                    # TODO
                    raise NotImplementedError("Completa LinkedList.add_head")

                def add_tail(self, item) -> None:
                    # TODO
                    raise NotImplementedError("Completa LinkedList.add_tail")

                def contains(self, item) -> bool:
                    # TODO
                    raise NotImplementedError("Completa LinkedList.contains")

                def size(self) -> int:
                    # TODO
                    raise NotImplementedError("Completa LinkedList.size")

                def remove_head(self):
                    # TODO: devuelve el elemento borrado o None si vacia
                    raise NotImplementedError("Completa LinkedList.remove_head")

                def remove_tail(self):
                    # TODO: devuelve el elemento borrado o None si vacia
                    raise NotImplementedError("Completa LinkedList.remove_tail")

                def to_list(self) -> list:
                    # TODO
                    raise NotImplementedError("Completa LinkedList.to_list")


            ll = LinkedList()
            assert ll.size() == 0
            assert ll.remove_head() is None
            assert ll.remove_tail() is None

            ll.add_head(4)
            ll.add_head(2)
            ll.add_tail(7)
            assert ll.to_list() == [2, 4, 7]
            assert ll.size() == 3
            assert ll.contains(4) is True
            assert ll.contains(9) is False
            assert ll.remove_head() == 2
            assert ll.to_list() == [4, 7]
            assert ll.remove_tail() == 7
            assert ll.to_list() == [4]
            assert ll.remove_tail() == 4
            assert ll.to_list() == []
            """
        ),
        md(
            """
            ## Mejoras y dunder methods

            No son obligatorias para cerrar la practica minima, pero debes saber que mejoran la interfaz:

            - `__len__`
            - `__contains__`
            - `__str__`
            """
        ),
        code(
            """
            ideas_dunder = ["__len__", "__contains__", "__str__"]
            assert "__len__" in ideas_dunder
            """
        ),
        md(
            """
            ## Comprobacion final

            No cierres el bloque hasta poder explicar:

            - que es `Node`
            - que es `head`
            - Como se recorre
            - por que Insertar en cabeza es mas simple que en cola
            - por que `remove_tail` necesita el penultimo
            - que Casos limite hay que comprobar
            """
        ),
        code(
            """
            checklist_final = {
                "node": False,
                "head": False,
                "recorrido": False,
                "insertar_en_cabeza": False,
                "penultimo_nodo": False,
                "casos_limite": False,
            }
            assert all(checklist_final.values()), "Cierra honestamente el checklist antes de salir del bloque."
            print("B06 listo para transferencia.")
            """
        ),
        md(
            """
            ## Cierre

            Cuando este cuaderno pase limpio con `Restart & Run All`, vuelve a tu repo de GitHub Classroom y cierra el bloque en [practica/06_linked_lists/ejercicios.py](../../practica/06_linked_lists/ejercicios.py). Si trabajas solo en navegador, usa `github.dev` con `.` y haz push para lanzar el autograding. Si trabajas en local, ejecuta despues `prueba.py`.
            """
        ),
    ]


def main() -> None:
    builders = {
        "01_fundamentos_python": ("B01 - Fundamentos de Python", b01),
        "02_clases_y_objetos": ("B02 - Clases y objetos", b02),
        "03_stacks_y_queues": ("B03 - ADT, stacks y queues", b03),
        "04_deque_priority_queue": ("B04 - Deque y priority queue", b04),
        "05_buffers_circulares": ("B05 - Buffers circulares", b05),
        "06_linked_lists": ("B06 - Linked lists", b06),
    }
    for folder, (title, builder) in builders.items():
        write_notebook(folder, title, builder())
        print(f"rebuilt {folder}")


if __name__ == "__main__":
    main()
