"""Pruebas simples para ejecutar desde Spyder."""

from ejercicios import BufferCircular


def run_tests() -> None:
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
    print("B05 OK")


if __name__ == "__main__":
    run_tests()
