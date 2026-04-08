"""Entrega acumulativa para Spyder.

Trabaja solo en este archivo.
Usa Ctrl+F para saltar a `===== B01 =====`, `===== B02 =====`, etc.
"""

from __future__ import annotations

from collections import deque


# ===== B01 =====
# Demuestra lectura de fichero, recorrido con enumerate y formato correcto de salida.

def cargar_numeros(path: str) -> list[int]:
    """
    Lee un fichero de texto con enteros separados por espacios y saltos de linea.

    Devuelve todos los enteros en una sola lista.
    """
    # TODO: implementar con open(...), strip(), split() e int(...)
    raise NotImplementedError("B01: completa cargar_numeros")


def etiquetar_con_indice(values: list[str]) -> list[str]:
    """
    Devuelve etiquetas tipo '0:a', '1:b', '2:c' usando enumerate.
    """
    # TODO: implementar usando enumerate
    raise NotImplementedError("B01: completa etiquetar_con_indice")


def formatear_media(nombre: str, media: float) -> str:
    """
    Devuelve un texto con la media formateada a 2 decimales.

    Ejemplo esperado:
    'Ana -> 7.50'
    """
    # TODO: implementar usando una f-string y formato de 2 decimales
    raise NotImplementedError("B01: completa formatear_media")


# ===== B02 =====
# Demuestra modelado basico con clases, metodos y encapsulacion sencilla.

class Estudiante:
    """
    Representa un estudiante con nombre, edad y nota.
    """

    def __init__(self, nombre: str, edad: int, nota: float):
        # TODO: asignar atributos
        raise NotImplementedError("B02: completa Estudiante.__init__")

    def es_aprobado(self) -> bool:
        # TODO: devolver True si nota >= 5
        raise NotImplementedError("B02: completa Estudiante.es_aprobado")

    def resumen(self) -> str:
        # TODO: devolver un texto tipo 'Ana (20) -> 8.50'
        raise NotImplementedError("B02: completa Estudiante.resumen")


class CuentaBancaria:
    """
    Cuenta bancaria simple con saldo interno protegido.
    """

    def __init__(self, titular: str, saldo_inicial: float):
        # TODO: guardar titular y __saldo
        raise NotImplementedError("B02: completa CuentaBancaria.__init__")

    def depositar(self, cantidad: float) -> None:
        # TODO
        raise NotImplementedError("B02: completa CuentaBancaria.depositar")

    def retirar(self, cantidad: float) -> bool:
        # TODO: devolver True si retira, False si no puede
        raise NotImplementedError("B02: completa CuentaBancaria.retirar")

    def saldo(self) -> float:
        # TODO
        raise NotImplementedError("B02: completa CuentaBancaria.saldo")


# ===== B03 =====
# Demuestra que distingues LIFO y FIFO y que puedes implementarlos con estado interno.

class Stack:
    def __init__(self):
        # TODO: usar una lista interna
        raise NotImplementedError("B03: completa Stack.__init__")

    def push(self, item) -> None:
        # TODO
        raise NotImplementedError("B03: completa Stack.push")

    def pop(self):
        # TODO
        raise NotImplementedError("B03: completa Stack.pop")

    def peek(self):
        # TODO
        raise NotImplementedError("B03: completa Stack.peek")

    def is_empty(self) -> bool:
        # TODO
        raise NotImplementedError("B03: completa Stack.is_empty")

    def size(self) -> int:
        # TODO
        raise NotImplementedError("B03: completa Stack.size")


class Queue:
    def __init__(self):
        # TODO: usar una lista interna
        raise NotImplementedError("B03: completa Queue.__init__")

    def enqueue(self, item) -> None:
        # TODO
        raise NotImplementedError("B03: completa Queue.enqueue")

    def dequeue(self):
        # TODO
        raise NotImplementedError("B03: completa Queue.dequeue")

    def peek(self):
        # TODO
        raise NotImplementedError("B03: completa Queue.peek")

    def is_empty(self) -> bool:
        # TODO
        raise NotImplementedError("B03: completa Queue.is_empty")

    def size(self) -> int:
        # TODO
        raise NotImplementedError("B03: completa Queue.size")


# ===== B04 =====
# Demuestra uso de deque y razonamiento sobre prioridad mediante orden interno.

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
    raise NotImplementedError("B04: completa aplicar_operaciones_deque")


class PriorityQueueOrdenada:
    """
    Priority queue sencilla donde la prioridad mas alta debe salir primero.
    """

    def __init__(self):
        # TODO: usa una lista interna
        raise NotImplementedError("B04: completa PriorityQueueOrdenada.__init__")

    def insertar(self, item: int) -> None:
        """
        Inserta manteniendo la lista interna ordenada de menor a mayor.
        """
        # TODO
        raise NotImplementedError("B04: completa PriorityQueueOrdenada.insertar")

    def extraer_maximo(self) -> int:
        """
        Devuelve y elimina el elemento con mayor prioridad.
        """
        # TODO
        raise NotImplementedError("B04: completa PriorityQueueOrdenada.extraer_maximo")

    def contenido(self) -> list[int]:
        # TODO
        raise NotImplementedError("B04: completa PriorityQueueOrdenada.contenido")


# ===== B05 =====
# Demuestra comprension de buffer circular, capacidad fija e indice de escritura.

class BufferCircular:
    """
    Buffer circular con politica de sobrescritura del dato mas antiguo.
    """

    def __init__(self, capacidad: int):
        # TODO: inicializa almacenamiento, indice de escritura y tamano actual
        raise NotImplementedError("B05: completa BufferCircular.__init__")

    def push(self, item) -> None:
        """
        Inserta un elemento.

        Si el buffer esta lleno, sobrescribe el dato mas antiguo.
        """
        # TODO
        raise NotImplementedError("B05: completa BufferCircular.push")

    def contenido(self) -> list:
        """
        Devuelve los elementos activos en orden FIFO.
        """
        # TODO
        raise NotImplementedError("B05: completa BufferCircular.contenido")


# ===== B06 =====
# Demuestra manejo de nodos, referencias y operaciones basicas sobre linked lists.

class Node:
    def __init__(self, data, next=None):
        # TODO
        raise NotImplementedError("B06: completa Node.__init__")


class LinkedList:
    def __init__(self):
        # TODO: guarda la cabeza
        raise NotImplementedError("B06: completa LinkedList.__init__")

    def add_head(self, item) -> None:
        # TODO
        raise NotImplementedError("B06: completa LinkedList.add_head")

    def add_tail(self, item) -> None:
        # TODO
        raise NotImplementedError("B06: completa LinkedList.add_tail")

    def contains(self, item) -> bool:
        # TODO
        raise NotImplementedError("B06: completa LinkedList.contains")

    def size(self) -> int:
        # TODO
        raise NotImplementedError("B06: completa LinkedList.size")

    def remove_head(self):
        # TODO: devuelve el elemento borrado o None si vacia
        raise NotImplementedError("B06: completa LinkedList.remove_head")

    def remove_tail(self):
        # TODO: devuelve el elemento borrado o None si vacia
        raise NotImplementedError("B06: completa LinkedList.remove_tail")

    def to_list(self) -> list:
        # TODO
        raise NotImplementedError("B06: completa LinkedList.to_list")
