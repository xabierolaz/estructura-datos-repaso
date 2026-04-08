"""Comprobador local y base del autograding.

No es la entrega. La entrega es `entrega_spyder.py`.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from entrega_spyder import (
    BufferCircular,
    CuentaBancaria,
    Estudiante,
    LinkedList,
    PriorityQueueOrdenada,
    Queue,
    Stack,
    aplicar_operaciones_deque,
    cargar_numeros,
    etiquetar_con_indice,
    formatear_media,
)


def run_b01() -> None:
    data_path = Path(__file__).parent / "datos" / "numbers.txt"
    assert cargar_numeros(str(data_path)) == [1, 2, 3, 4, 5, 6, 7], "B01: revisa lectura de fichero, split e int"
    assert etiquetar_con_indice(["a", "b", "c"]) == ["0:a", "1:b", "2:c"], "B01: revisa enumerate"
    assert formatear_media("Ana", 7.5) == "Ana -> 7.50", "B01: revisa f-string y formato"
    assert formatear_media("Luis", 8) == "Luis -> 8.00", "B01: revisa formato a 2 decimales"


def run_b02() -> None:
    estudiante = Estudiante("Ana", 20, 8.5)
    assert estudiante.nombre == "Ana", "B02: nombre no queda guardado"
    assert estudiante.edad == 20, "B02: edad no queda guardada"
    assert estudiante.nota == 8.5, "B02: nota no queda guardada"
    assert estudiante.es_aprobado() is True, "B02: revisa condicion de aprobado"
    assert estudiante.resumen() == "Ana (20) -> 8.50", "B02: revisa resumen y formato"

    cuenta = CuentaBancaria("Ana", 100)
    assert cuenta.saldo() == 100, "B02: saldo inicial incorrecto"
    cuenta.depositar(50)
    assert cuenta.saldo() == 150, "B02: depositar no actualiza saldo"
    assert cuenta.retirar(20) is True, "B02: retirar valido deberia devolver True"
    assert cuenta.saldo() == 130, "B02: retirar no descuenta correctamente"
    assert cuenta.retirar(200) is False, "B02: no debe permitir retirar mas de lo disponible"
    assert cuenta.saldo() == 130, "B02: saldo no debe cambiar si la retirada falla"


def run_b03() -> None:
    s = Stack()
    assert s.is_empty() is True, "B03: Stack vacio debe reportarse vacio"
    s.push(4)
    s.push(9)
    s.push(2)
    assert s.size() == 3, "B03: Stack size incorrecto"
    assert s.peek() == 2, "B03: Stack debe ser LIFO"
    assert s.pop() == 2, "B03: Stack pop incorrecto"
    assert s.peek() == 9, "B03: Stack peek tras pop incorrecto"
    assert s.size() == 2, "B03: Stack size tras pop incorrecto"

    q = Queue()
    assert q.is_empty() is True, "B03: Queue vacia debe reportarse vacia"
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    assert q.size() == 3, "B03: Queue size incorrecto"
    assert q.peek() == "A", "B03: Queue debe ser FIFO"
    assert q.dequeue() == "A", "B03: Queue dequeue incorrecto"
    assert q.peek() == "B", "B03: Queue peek tras dequeue incorrecto"
    assert q.size() == 2, "B03: Queue size tras dequeue incorrecto"


def run_b04() -> None:
    ops = [
        ("append", "b"),
        ("appendleft", "a"),
        ("append", "c"),
        ("popleft", None),
    ]
    assert aplicar_operaciones_deque(ops) == ["b", "c"], "B04: revisa operaciones sobre deque"

    pq = PriorityQueueOrdenada()
    for value in [3, 1, 5, 2]:
        pq.insertar(value)
    assert pq.contenido() == [1, 2, 3, 5], "B04: la cola prioritaria debe quedar ordenada"
    assert pq.extraer_maximo() == 5, "B04: el maximo debe salir primero"
    assert pq.extraer_maximo() == 3, "B04: la segunda extraccion es incorrecta"
    assert pq.contenido() == [1, 2], "B04: contenido restante incorrecto"


def run_b05() -> None:
    b = BufferCircular(3)
    b.push(1)
    b.push(2)
    assert b.contenido() == [1, 2], "B05: contenido parcial incorrecto"
    b.push(3)
    assert b.contenido() == [1, 2, 3], "B05: contenido lleno incorrecto"
    b.push(4)
    assert b.contenido() == [2, 3, 4], "B05: debe sobrescribir el dato mas antiguo"
    b.push(5)
    assert b.contenido() == [3, 4, 5], "B05: orden FIFO incorrecto tras varias sobrescrituras"


def run_b06() -> None:
    ll = LinkedList()
    assert ll.size() == 0, "B06: size inicial debe ser 0"
    assert ll.remove_head() is None, "B06: remove_head sobre lista vacia debe devolver None"
    assert ll.remove_tail() is None, "B06: remove_tail sobre lista vacia debe devolver None"

    ll.add_head(4)
    ll.add_head(2)
    ll.add_tail(7)
    assert ll.to_list() == [2, 4, 7], "B06: inserciones en cabeza/cola incorrectas"
    assert ll.size() == 3, "B06: size incorrecto"
    assert ll.contains(4) is True, "B06: contains no encuentra un valor presente"
    assert ll.contains(9) is False, "B06: contains no deberia encontrar un valor ausente"
    assert ll.remove_head() == 2, "B06: remove_head incorrecto"
    assert ll.to_list() == [4, 7], "B06: estado incorrecto tras remove_head"
    assert ll.remove_tail() == 7, "B06: remove_tail incorrecto"
    assert ll.to_list() == [4], "B06: estado incorrecto tras remove_tail"
    assert ll.remove_tail() == 4, "B06: remove_tail final incorrecto"
    assert ll.to_list() == [], "B06: la lista deberia quedar vacia"


BLOCKS = {
    "B01": ("Fundamentos de Python", run_b01),
    "B02": ("Clases y objetos", run_b02),
    "B03": ("Stacks y queues", run_b03),
    "B04": ("Deque y priority queue", run_b04),
    "B05": ("Buffers circulares", run_b05),
    "B06": ("Linked lists", run_b06),
}


def run_selected(block_keys: list[str]) -> int:
    failures: list[str] = []
    for key in block_keys:
        label, fn = BLOCKS[key]
        try:
            fn()
        except Exception as exc:
            print(f"{key} FAIL - {label}")
            print(f"  {exc}")
            failures.append(key)
        else:
            print(f"{key} OK - {label}")
    if failures:
        print("\nResumen: revisa los bloques marcados como FAIL y vuelve al cuaderno correspondiente.")
        return 1
    print("\nTodo OK.")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Comprobador por bloques de la entrega unica.")
    parser.add_argument("--block", choices=sorted(BLOCKS), help="Ejecuta solo un bloque concreto.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.block:
        return run_selected([args.block])
    return run_selected(sorted(BLOCKS))


if __name__ == "__main__":
    sys.exit(main())
