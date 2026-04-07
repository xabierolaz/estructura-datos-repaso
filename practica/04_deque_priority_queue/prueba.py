"""Pruebas simples para ejecutar desde Spyder."""

from ejercicios import PriorityQueueOrdenada, aplicar_operaciones_deque


def probar_deque() -> None:
    ops = [
        ("append", "b"),
        ("appendleft", "a"),
        ("append", "c"),
        ("popleft", None),
    ]
    assert aplicar_operaciones_deque(ops) == ["b", "c"]


def probar_priority_queue() -> None:
    pq = PriorityQueueOrdenada()
    for value in [3, 1, 5, 2]:
        pq.insertar(value)
    assert pq.contenido() == [1, 2, 3, 5]
    assert pq.extraer_maximo() == 5
    assert pq.extraer_maximo() == 3
    assert pq.contenido() == [1, 2]


def run_tests() -> None:
    probar_deque()
    probar_priority_queue()
    print("B04 OK")


if __name__ == "__main__":
    run_tests()
