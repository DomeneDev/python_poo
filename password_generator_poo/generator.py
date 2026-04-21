"""
Módulo de Generación - El Cerebro

Este módulo contiene la lógica central para la creación de contraseñas.
Implementa los diferentes niveles de seguridad (Ockham 1, 2, 3) y se
encarga de la selección aleatoria de caracteres basada en la longitud solicitada.
"""

# Importamos biblioteca string para mapear los caracteres
import string
# Importamos random para generar posiciones aleatorias
import random


class Generador:
    """
    Motor de generación de credenciales robustas.

    Esta clase implementa la lógica de creación de contraseñas aleatorias
    basada en una jerarquía de niveles de seguridad. Utiliza entropía
    proporcionada por el módulo 'random' y conjuntos de caracteres
    estandarizados del módulo 'string'.

    Attributes:
        mapa_caracteres(dict): Diccionario que vincula los niveles de
        seguridad(1, 2, 3) con sus respectivos pools de caracteres.
    """

    def __init__(self):
        self.mapa_caracteres = {1: string.digits, 2: string.digits + string.ascii_letters,
                                3: string.digits + string.ascii_letters + string.punctuation}

    def generar(self, nivel: int, longitud: int) -> str:
        """
        Generar contraseña según el nivel y longitud indicadas

        Args:
            nivel (int): Nivel de contraseña
            longitud (int): Longitud de contraseña

        Returns:
            str: Contraseña generada con los parámetros indicados.
        """
        caracteres_passworod = random.choices(
            self.mapa_caracteres[nivel], k=longitud)
        password = "".join(caracteres_passworod)
        return password
