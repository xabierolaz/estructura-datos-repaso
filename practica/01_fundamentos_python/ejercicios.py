"""Ejercicios de B01 listos para abrir en Spyder."""

from pathlib import Path


def cargar_numeros(path: str) -> list[int]:
    """
    Lee un fichero de texto con enteros separados por espacios y saltos de linea.

    Devuelve todos los enteros en una sola lista.
    """
    # TODO: implementar con open(...), strip(), split() e int(...)
    raise NotImplementedError("Completa cargar_numeros")


def etiquetar_con_indice(values: list[str]) -> list[str]:
    """
    Devuelve etiquetas tipo '0:a', '1:b', '2:c' usando enumerate.
    """
    # TODO: implementar usando enumerate
    raise NotImplementedError("Completa etiquetar_con_indice")


def formatear_media(nombre: str, media: float) -> str:
    """
    Devuelve un texto con la media formateada a 2 decimales.

    Ejemplo esperado:
    'Ana -> 7.50'
    """
    # TODO: implementar usando una f-string y formato de 2 decimales
    raise NotImplementedError("Completa formatear_media")


def main() -> None:
    data_path = Path(__file__).parent / "datos" / "numbers.txt"
    numeros = cargar_numeros(str(data_path))
    print("Numeros:", numeros)
    print(etiquetar_con_indice(["a", "b", "c"]))
    print(formatear_media("Ana", 7.5))


if __name__ == "__main__":
    main()
