"""Ejercicios de B02 listos para abrir en Spyder."""


class Estudiante:
    """
    Representa un estudiante con nombre, edad y nota.

    Requisitos:
    - guardar esos tres atributos
    - implementar es_aprobado()
    - implementar resumen()
    """

    def __init__(self, nombre: str, edad: int, nota: float):
        # TODO: asignar atributos
        raise NotImplementedError("Completa Estudiante.__init__")

    def es_aprobado(self) -> bool:
        # TODO: devolver True si nota >= 5
        raise NotImplementedError("Completa Estudiante.es_aprobado")

    def resumen(self) -> str:
        # TODO: devolver un texto tipo 'Ana (20) -> 8.50'
        raise NotImplementedError("Completa Estudiante.resumen")


class CuentaBancaria:
    """
    Cuenta bancaria simple con saldo interno protegido.

    Requisitos:
    - usar __saldo como atributo interno
    - depositar(cantidad) suma saldo si cantidad > 0
    - retirar(cantidad) resta saldo solo si cantidad > 0 y hay dinero suficiente
    - saldo() devuelve el saldo actual
    """

    def __init__(self, titular: str, saldo_inicial: float):
        # TODO: guardar titular y __saldo
        raise NotImplementedError("Completa CuentaBancaria.__init__")

    def depositar(self, cantidad: float) -> None:
        # TODO
        raise NotImplementedError("Completa CuentaBancaria.depositar")

    def retirar(self, cantidad: float) -> bool:
        # TODO: devolver True si retira, False si no puede
        raise NotImplementedError("Completa CuentaBancaria.retirar")

    def saldo(self) -> float:
        # TODO
        raise NotImplementedError("Completa CuentaBancaria.saldo")
