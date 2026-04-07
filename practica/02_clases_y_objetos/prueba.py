"""Pruebas simples para ejecutar desde Spyder."""

from ejercicios import CuentaBancaria, Estudiante


def run_tests() -> None:
    estudiante = Estudiante("Ana", 20, 8.5)
    assert estudiante.nombre == "Ana"
    assert estudiante.edad == 20
    assert estudiante.nota == 8.5
    assert estudiante.es_aprobado() is True
    assert estudiante.resumen() == "Ana (20) -> 8.50"

    cuenta = CuentaBancaria("Ana", 100)
    assert cuenta.saldo() == 100
    cuenta.depositar(50)
    assert cuenta.saldo() == 150
    assert cuenta.retirar(20) is True
    assert cuenta.saldo() == 130
    assert cuenta.retirar(200) is False
    assert cuenta.saldo() == 130
    print("B02 OK")


if __name__ == "__main__":
    run_tests()
