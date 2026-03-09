"""
Módulo de Modelos de Datos - Analizador de Texto POO

Este módulo contiene las definiciones de las clases que actúan como 
contenedores de información. Se centra en la representación y 
almacenamiento de los estados del análisis.

Clases:
    ResultadoAnalisis: Representa el informe final de un procesamiento de texto.
"""
# Importamos libraría datetime para anotar marcas de tiempo
from datetime import datetime


class ResultadosAnalisis:
    """
    Clase contendor, almacena y presenta los resultados de un análisis
    """

    def __init__(self, texto_original: str, total_palabras: int, total_caracteres: int):
        """
        Constructor que inicializa los atributos

        Args:
            texto_original (str):
            total_palabras (int):
            total_caracteres (int)
        """
        self.texto = texto_original
        self.palabras = total_palabras
        self.caracteres = total_caracteres
        # Marca de tiempo del analisis
        self.fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def __str__(self):
        """
        Método para imprimir de forma estructurada el resultado del analisis
        """
        return (
            f"\n 🧾 --- INFORMA DE ANALISIS ---\n"
            f"📆 Fecha: {self.fecha}\n"
            f"📋 Texto: {self.texto[:30]}\n"
            f"🔢 Palabras: {self.palabras}\n"
            f"🔠 Caracteres: {self.caracteres}\n"
        )
