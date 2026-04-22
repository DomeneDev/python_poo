"""
Módulo de Entidad - La Nota

Este módulo define la clase Nota, que representa la unidad básica de
información del sistema. Se encarga de la estructura de datos y de
la representación textual de una nota individual.
"""

# Importamos datetime para establecer fecha de creación automáticas
from datetime import datetime


class Nota:
    """
    Representa una nota dentro del sistema
    """

    def __init__(self, titulo: str, descripcion: str, fecha: str = None):
        """
        Constructor de la nota

        Args:
            titulo (str): Titulo de la Nota
            descripcion (str): Descripción de la nota

        La marca de tiempo se generará automáticamente dentro del constructor
        """
        self.titulo = titulo
        self.descripcion = descripcion
        if fecha:
            self.fecha = fecha
        else:
            self.fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def __str__(self) -> str:
        """
        Genera una representación visual de la nota

        Returns:
            str: Nota con formato de salida
        """
        return (
            f"Titulo: {self.titulo}\n"
            f"📅 Creada: {self.fecha}\n"
            f"📝 Descripción:\n\t{self.descripcion}\n"
            f"{'-'*40}\n"
        )
