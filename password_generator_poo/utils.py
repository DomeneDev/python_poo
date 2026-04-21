"""
Módulo de Utilidades - Herramientas de Soporte

Contiene funciones auxiliares para la validación de entradas por teclado,
asegurando que el usuario cumpla con los rangos establecidos para niveles
y longitud, además de gestionar posibles errores de ejecución.
"""


def validar_nivel(msg_input: str, msg_error: str) -> int:
    """
    Función para seleccionar nivel de contraseña.
    Nivel 1 : Sólo números
    Nivel 2 : Números y letras (MAYÚSCULAS Y minúsculas)
    Nivel 3 : Números, letras (MAYÚSCULAS Y minúsculas) y carácteres espciales

    Args:
        msg_input (str): Mensaje de input
        msg_error (str): Mensaje de error

    Returns:
        int: Nivel de contraseña válido
    """
    niveles_validos = [1, 2, 3]
    while True:
        try:
            nivel = int(input(msg_input))
            if nivel in niveles_validos:
                break
            else:
                print(msg_error)
        except ValueError:
            print(msg_error)
    return nivel


def establecer_longitud(msg_input: str, msg_error: str) -> int:
    """
    Función para establcer longitud de la contraseña
    Debe encontrarse entre 8 y 50

    Args:
        msg_input (str): Mensaje de input
        msg_error (str): Mensaje de error

    Returns:
        int: Longitud de la contraseña en rango establecido.
    """
    while True:
        try:
            longitud = int(input(msg_input))
            if 8 <= longitud <= 50:
                break
            else:
                print(msg_error)
        except ValueError:
            print(msg_error)
    return longitud


def menu():
    """
    Función para mostrar el menú de la app
    """
    print("+---------------------------------+")
    print("|  🔐  Generador de contraseñas   |")
    print("+---------------------------------+")
    print("| 1 - Generar contraseña          |")
    print("| 2 - Salir                       |")
    print("+---------------------------------+")


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
