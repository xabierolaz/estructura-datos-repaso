"""Entrega acumulativa para Spyder.

Trabaja solo en este archivo.
Usa Ctrl+F para saltar a `===== B01 =====`, `===== B02 =====`, etc.

La correccion es por bloques:
- un bloque flojo no se compensa con otro
- la teoria debe demostrarse en codigo
"""

from __future__ import annotations

from collections import deque


# ===== B01 =====
# Demuestra lectura de fichero, recorrido con enumerate, desempaquetado
# y transformacion correcta de texto a datos.

def cargar_numeros(path: str) -> list[int]:
    """
    Lee un fichero con enteros separados por espacios y saltos de linea.

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


def separar_extremos(values: list[int]) -> tuple[int, list[int], int]:
    """
    Separa el primer elemento, los del medio y el ultimo.

    Ejemplo:
    [10, 20, 30, 40] -> (10, [20, 30], 40)
    """
    # TODO: usar desempaquetado con *
    raise NotImplementedError("B01: completa separar_extremos")


def sumar_lineas(path: str) -> list[int]:
    """
    Lee un fichero y devuelve la suma de enteros de cada linea no vacia.

    Ejemplo:
    '1 2 3\\n4 5\\n' -> [6, 9]
    """
    # TODO: leer linea a linea, aplicar strip(), split(), int(...) y sumar
    raise NotImplementedError("B01: completa sumar_lineas")


# ===== B02 =====
# Demuestra modelado con clases, metodos, encapsulacion e invariantes basicos.

class Estudiante:
    """
    Representa un estudiante con nombre, edad y nota.

    Invariantes:
    - edad >= 0
    - 0 <= nota <= 10
    """

    def __init__(self, nombre: str, edad: int, nota: float):
        # TODO: validar invariantes y asignar atributos
        raise NotImplementedError("B02: completa Estudiante.__init__")

    def es_aprobado(self) -> bool:
        # TODO: devolver True si nota >= 5
        raise NotImplementedError("B02: completa Estudiante.es_aprobado")

    def resumen(self) -> str:
        # TODO: devolver un texto tipo 'Ana (20) -> 8.50'
        raise NotImplementedError("B02: completa Estudiante.resumen")

    def actualizar_nota(self, nueva_nota: float) -> bool:
        """
        Actualiza la nota si sigue el invariante.

        Devuelve True si actualiza y False si no.
        """
        # TODO
        raise NotImplementedError("B02: completa Estudiante.actualizar_nota")


class CuentaBancaria:
    """
    Cuenta bancaria simple con saldo interno protegido.

    Invariante:
    - el saldo nunca debe quedar negativo
    """

    def __init__(self, titular: str, saldo_inicial: float):
        # TODO: guardar titular y __saldo; saldo inicial no puede ser negativo
        raise NotImplementedError("B02: completa CuentaBancaria.__init__")

    def depositar(self, cantidad: float) -> None:
        # TODO: exigir cantidad positiva
        raise NotImplementedError("B02: completa CuentaBancaria.depositar")

    def retirar(self, cantidad: float) -> bool:
        # TODO: devolver True si retira, False si no puede
        raise NotImplementedError("B02: completa CuentaBancaria.retirar")

    def saldo(self) -> float:
        # TODO
        raise NotImplementedError("B02: completa CuentaBancaria.saldo")

    def resumen(self) -> str:
        # TODO: devolver un texto tipo 'Ana -> 120.50'
        raise NotImplementedError("B02: completa CuentaBancaria.resumen")


# ===== B03 =====
# Demuestra que distingues LIFO y FIFO y que puedes convertir esa teoria en comportamiento.

class Stack:
    def __init__(self):
        # TODO: usar una lista interna
        raise NotImplementedError("B03: completa Stack.__init__")

    def push(self, item) -> None:
        # TODO
        raise NotImplementedError("B03: completa Stack.push")

    def pop(self):
        # TODO: devolver None si esta vacia
        raise NotImplementedError("B03: completa Stack.pop")

    def peek(self):
        # TODO: devolver None si esta vacia
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
        # TODO: devolver None si esta vacia
        raise NotImplementedError("B03: completa Queue.dequeue")

    def peek(self):
        # TODO: devolver None si esta vacia
        raise NotImplementedError("B03: completa Queue.peek")

    def is_empty(self) -> bool:
        # TODO
        raise NotImplementedError("B03: completa Queue.is_empty")

    def size(self) -> int:
        # TODO
        raise NotImplementedError("B03: completa Queue.size")


def orden_salida_lifo_fifo(values: list[object]) -> tuple[list[object], list[object]]:
    """
    Inserta todos los elementos en una stack y en una queue.

    Devuelve:
    - la salida completa al vaciar la stack
    - la salida completa al vaciar la queue
    """
    # TODO: usar Stack y Queue para hacer visible la diferencia de comportamiento
    raise NotImplementedError("B03: completa orden_salida_lifo_fifo")


# ===== B04 =====
# Demuestra uso de deque y comparacion real entre dos implementaciones de priority queue.

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
    Priority queue donde el trabajo fuerte se paga al insertar.
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

    def extraer_maximo(self) -> int | None:
        """
        Devuelve y elimina el elemento con mayor prioridad.
        """
        # TODO
        raise NotImplementedError("B04: completa PriorityQueueOrdenada.extraer_maximo")

    def contenido(self) -> list[int]:
        # TODO
        raise NotImplementedError("B04: completa PriorityQueueOrdenada.contenido")


class PriorityQueueBusqueda:
    """
    Priority queue donde insertar es facil y buscar el maximo se paga al extraer.
    """

    def __init__(self):
        # TODO: usa una lista interna sin mantenerla ordenada
        raise NotImplementedError("B04: completa PriorityQueueBusqueda.__init__")

    def insertar(self, item: int) -> None:
        # TODO
        raise NotImplementedError("B04: completa PriorityQueueBusqueda.insertar")

    def extraer_maximo(self) -> int | None:
        # TODO: localizar el maximo, eliminarlo y devolverlo
        raise NotImplementedError("B04: completa PriorityQueueBusqueda.extraer_maximo")

    def contenido(self) -> list[int]:
        # TODO
        raise NotImplementedError("B04: completa PriorityQueueBusqueda.contenido")


# ===== B05 =====
# Demuestra buffer circular con capacidad fija y dos politicas cuando se llena.

class BufferCircular:
    """
    Buffer circular con dos politicas soportadas:
    - 'overwrite': sobrescribe el dato mas antiguo
    - 'drop': ignora el dato nuevo cuando esta lleno
    """

    def __init__(self, capacidad: int, politica: str = "overwrite"):
        # TODO: validar capacidad/politica e inicializar almacenamiento e indices
        raise NotImplementedError("B05: completa BufferCircular.__init__")

    def push(self, item) -> None:
        """
        Inserta un elemento respetando la politica del buffer.
        """
        # TODO
        raise NotImplementedError("B05: completa BufferCircular.push")

    def contenido(self) -> list:
        """
        Devuelve los elementos activos en orden FIFO.
        """
        # TODO
        raise NotImplementedError("B05: completa BufferCircular.contenido")

    def politica(self) -> str:
        # TODO
        raise NotImplementedError("B05: completa BufferCircular.politica")

    def capacidad(self) -> int:
        # TODO
        raise NotImplementedError("B05: completa BufferCircular.capacidad")


# ===== B06 =====
# Demuestra manejo de nodos, referencias, casos limite y mejoras de integracion con Python.

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

    def get(self, index: int):
        """
        Devuelve el elemento del indice indicado o None si no existe.
        """
        # TODO
        raise NotImplementedError("B06: completa LinkedList.get")

    def set(self, index: int, value) -> bool:
        """
        Sustituye el valor del nodo en `index`.

        Devuelve True si actualiza y False si no.
        """
        # TODO
        raise NotImplementedError("B06: completa LinkedList.set")

    def remove_head(self):
        # TODO: devuelve el elemento borrado o None si vacia
        raise NotImplementedError("B06: completa LinkedList.remove_head")

    def remove_tail(self):
        # TODO: devuelve el elemento borrado o None si vacia
        raise NotImplementedError("B06: completa LinkedList.remove_tail")

    def to_list(self) -> list:
        # TODO
        raise NotImplementedError("B06: completa LinkedList.to_list")

    def __len__(self) -> int:
        # TODO: reutiliza size()
        raise NotImplementedError("B06: completa LinkedList.__len__")

    def __str__(self) -> str:
        # TODO: devolver una representacion tipo '[2, 4, 7]'
        raise NotImplementedError("B06: completa LinkedList.__str__")
