"""Pruebas simples para ejecutar desde Spyder."""

from pathlib import Path

from ejercicios import cargar_numeros, etiquetar_con_indice, formatear_media


def run_tests() -> None:
    data_path = Path(__file__).parent / "datos" / "numbers.txt"
    assert cargar_numeros(str(data_path)) == [1, 2, 3, 4, 5, 6, 7]
    assert etiquetar_con_indice(["a", "b", "c"]) == ["0:a", "1:b", "2:c"]
    assert formatear_media("Ana", 7.5) == "Ana -> 7.50"
    assert formatear_media("Luis", 8) == "Luis -> 8.00"
    print("B01 OK")


if __name__ == "__main__":
    run_tests()
