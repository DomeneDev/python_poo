"""
Módulo de Lógica de negocio

Este modulo define la lógica para gestionar la colección de objetos
Movimiento, Esta clase separará la lógica del cálculo de la simple
representación de los datos
"""


class CalculadoraPresupuesto:
    """
    Clase para cálculos relacionado con los movimientos
    """

    def __init__(self):
        """
        Método constructor para almacenar los movimientos, una lista vacía
        """
        self._historial = []

    def registrar_movimiento(self, movimiento: object):
        """
        Método para almacenar movimientos, recibe un objeto movimiento
        y lo añade a la lista del constructor

        Args:
            movimiento (object): Movimiento
        """
        self._historial.append(movimiento)

    def calcular_balance(self) -> float:
        """
        Calcular blance de los movimientos

        Args:
            _hisotorial (list): Historial de movimientos

        Return
            balance (float): balance con formato 2 decimales
        """
        ingreso = 0
        gasto = 0
        for movimiento in self._historial:
            if movimiento.tipo == "Ingreso":
                ingreso += movimiento.cantidad
            else:
                gasto += movimiento.cantidad
        balance = round(ingreso - gasto, 2)
        return balance

    def generar_informe(self) -> str:
        """
        Método para generar informe de todos los movimientos con sus detalles
        Asi como del balance total

        Args:
            _historial (list): Lista de movimientos

        Returns:
            str: Informe con formato
        """
        for movimiento in self._historial:
            if movimiento.tipo == "Ingreso":
                print(f"🟢 {movimiento}")
            else:
                print(f"🔴 {movimiento}")
        print(f"Balance total: {self.calcular_balance()}")
