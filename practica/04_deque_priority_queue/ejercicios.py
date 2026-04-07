"""Ejercicios de B04 listos para abrir en Spyder."""

from collections import deque


def aplicar_operaciones_deque(operaciones: list[tuple[str, object]]) -> list[object]:
    """
    Aplica operaciones sobre una deque y devuelve su contenido final como lista.

    Operaciones validas:
    - ("append", valor)
    - ("appendleft", valor)
    - ("pop", None)
    - ("popleft", None)
    """
    # TODO: usar collections.deque y devolver list(d)
    raise NotImplementedError("Completa aplicar_operaciones_deque")


class PriorityQueueOrdenada:
    """
    Priority queue sencilla donde la prioridad mas alta debe salir primero.
    """

    def __init__(self):
        # TODO: usa una lista interna
        raise NotImplementedError("Completa PriorityQueueOrdenada.__init__")

    def insertar(self, item: int) -> None:
        """
        Inserta manteniendo la lista interna ordenada de menor a mayor.
        """
        # TODO
        raise NotImplementedError("Completa PriorityQueueOrdenada.insertar")

    def extraer_maximo(self) -> int:
        """
        Devuelve y elimina el elemento con mayor prioridad.
        """
        # TODO
        raise NotImplementedError("Completa PriorityQueueOrdenada.extraer_maximo")

    def contenido(self) -> list[int]:
        # TODO
        raise NotImplementedError("Completa PriorityQueueOrdenada.contenido")
