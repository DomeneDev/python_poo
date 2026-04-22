"""
Módulo de Utilidades - Herramientas de Interfaz

Proporciona funciones auxiliares para la validación de entradas del usuario,
formateo de fechas y limpieza de la consola para mejorar la experiencia de usuario.
"""


def menu():
    """
    Funcióm para mostra menú
    """
    print("<---------------------------->")
    print("|  📝 Gestor de notas       |")
    print("<---------------------------->")
    print("| 1 - Añadir notas 🧾        |")
    print("| 2 - Listar notas 📋        |")
    print("| 3 - Eliminar notas 🗑       |")
    print("| 4 - Salir 🚪               |")
    print("<---------------------------->")


def validar_opcion(msg_input: str, msg_error: str) -> int:
    """
    Función verificar opción de entrada

    Args:
        msg_input (str): Mensaje de input
        msg_error (str): Mensaje de error

    Returns:
        int: Opción validada
    """
    while True:
        try:
            opcion = input(msg_input)
            opcion = int(opcion)
            break
        except ValueError:
            print(msg_error)
    return opcion


def formatear_cadenas(msg_input: str, msg_error_vacio) -> str:
    """
    Función para dar formato a cadenas

    Args:
        msg_input (str): Mensaje de input

    Returns:
        str: cadena con formato captilize()
    """
    while True:
        cadena = input(msg_input).strip()
        if not cadena:
            print(msg_error_vacio)
        else:
            return cadena.capitalize()
