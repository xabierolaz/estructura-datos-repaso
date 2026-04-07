"""Ejercicios de B06 listos para abrir en Spyder."""


class Node:
    def __init__(self, data, next=None):
        # TODO
        raise NotImplementedError("Completa Node.__init__")


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
