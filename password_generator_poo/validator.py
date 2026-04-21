"""
Módulo de Auditoría - El Validador

Este módulo se encarga de analizar la robustez de las contraseñas generadas.
Proporciona una capa de seguridad adicional evaluando factores como
la longitud y la entropía de los caracteres utilizados.
"""

# Importamos string para poder comparar los signos de puntuación
import string


def evaluar_seguridad(password_generado: str) -> str:
    """
    Función para evaluar la seguridad de la contraseña.
    Criterios:
    - Si la longitud es > 12 -> + 1 punto.
    - Si tiene algún número -> + 1 punto.
    - Si tiene mayúsculas y minusculas ->+ 1 punto.
    - Si tiene caracteres especiales -> + 1 punto.

    Veredicto:
    - 0-2 puntos: Baja
    - 3 puntos: Media
    - 4 puntos: Alta

    Args:
        password_generado (str): contraseña generada por generator

    Returns:
        str: Veredicto
    """
    puntos = 0
    if len(password_generado) > 12:
        puntos += 1
    if any(c.isdigit() for c in password_generado):
        puntos += 1
    if any(c.isupper() for c in password_generado):
        puntos += 1
    if any(c in string.punctuation for c in password_generado):
        puntos += 1

    if 0 <= puntos <= 2:
        return "🔴 Baja"
    elif puntos == 3:
        return "🟡 Media"
    elif puntos == 4:
        return "🟢 Alta"
