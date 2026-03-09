"""
Módulo de Lógica de Negocio - Motor de Análisis

Este módulo define la lógica encargada de transformar cadenas de texto
en objetos de datos enriquecidos. Utiliza un enfoque orientado a objetos
para encapsular el comportamiento del análisis.

Clases:
    MotorAnalizador: Orquestador del procesamiento y conteo de métricas.
"""
# Importamos de models.py la Clase de ResultadosAnalisis
from models import ResultadosAnalisis


class MotorAnalizador:
    """
    Clase Motor Analizador, recibe el texto y ejecuta el analisis
    devolviendo un objeto ResultadoAnalisis
    """

    def __init__(self, texto):
        """
        Método constructor

        Args:
            texto (_type_):
        """
        self.texto = texto.strip()

    def ejecutar(self) -> ResultadosAnalisis:
        """
        Realiza análisis y devuelve un OBJTO de tipo ResultadosAnalisis.

        Returns:
            ResultadosAnalisis
        """
        # Almacenamos los resultados de palabra y caracteres en variables
        palabras = len(self.texto.split())
        caracteres = len(self.texto)
        # Devolvemos una instacia de nuestra clase de datos
        return ResultadosAnalisis(self.texto, palabras, caracteres)
