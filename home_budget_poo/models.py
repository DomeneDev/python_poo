"""
Módulo de modelo de Movimiento
"""

# Impotamos libería date time para aontar marcas de tiempo
from datetime import datetime


class Movimiento():
    """
    Clase Movimiento para generar objetos tipo movimiento
    """

    def __init__(self, concepto: str, cantidad: float, categoria: str, tipo: str):
        """
        Constructor de objetos movimiento

        Args:
            concepto (str): Concepto del movimiento
            cantidad (float): Cantidad del movimiento
            categoria (str): Categoria del movimiento
            tipo (str): Tipo del movimiento
        """
        self.concepto = self._formato_cadenas(concepto)
        self.cantidad = self._limpiar_cantidad(cantidad)
        self.categoria = self._formato_cadenas(categoria)
        self.tipo = self._formato_cadenas(tipo)
        # Marca de tiempo para la anotación
        self.fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Métodos para limpiar datos sensibles
    def _limpiar_cantidad(self, cantidad: float) -> float:
        """
        Método para limpiar el valor negativo de la cantidad, para evitar
        errores en operaciones matemáticas posteriores

        Args:
            cantidad (float): Valor monterio del gasto

        Returns:
            float: Valor monetario del gasto limpio
        """
        if cantidad < 0:
            return abs(cantidad)
        else:
            return cantidad

    def _formato_cadenas(self, cadena: str) -> str:
        """
        Método para dar formato al tipo de movimiento.
        Formato aceptado: title

        Args:
            tipo (str): Tipo de movimiento sin formato

        Returns:
            str: Tipo de movimiento con formato
        """
        cadena = cadena.strip()
        cadena = cadena.title()
        return cadena

    def __str__(self):
        """
        Método para imprimir movimiento con formato
        """
        return (
            f" - [{self.tipo}] - {self.fecha} | {self.categoria}: {self.cantidad}"
        )
