"""Ejercicios de B05 listos para abrir en Spyder."""


class BufferCircular:
    """
    Buffer circular con politica de sobrescritura del dato mas antiguo.
    """

    def __init__(self, capacidad: int):
        # TODO: inicializa almacenamiento, indice de escritura y tamano actual
        raise NotImplementedError("Completa BufferCircular.__init__")

    def push(self, item) -> None:
        """
        Inserta un elemento.

        Si el buffer esta lleno, sobrescribe el dato mas antiguo.
        """
        # TODO
        raise NotImplementedError("Completa BufferCircular.push")

    def contenido(self) -> list:
        """
        Devuelve los elementos activos en orden FIFO.
        """
        # TODO
        raise NotImplementedError("Completa BufferCircular.contenido")
