"""
Modulo para lógica de apoyo de main
"""


def menu():
    """
    Función para mostrar menú
    """
    # Menu de acciones de la app
    print("+-----------------------------------+")
    print("|  ✍ Gestor de tareas 2.0          |")
    print("+-----------------------------------+")
    print("| 1 - Agregar tarea.                |")
    print("| 2 - Actualizar tarea.             |")
    print("| 3 - Elminar tarea.                |")
    print("| 4 - Mostrar tareas.               |")
    print("| 5 - Salir.                        |")
    print("+-----------------------------------+\n")


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


def validar_estado(msg_input: str, msg_error_vacio: str, msg_error_estado_no_valido) -> str:
    """
    Función para verificar el estado de las tarea en formato correcto.
    Solo aceptará valores permitidos.

    Args:
        msg_input (str): Mensaje de input
        msg_error_vacio (str): Mensaje de error cadena vacia
        msg_error_estado_no_valido (str): Mensaje de error estado no valido

    Returns:
        str: Estado valido.
    """
    estados_permitidos = ["en curso", "finalizada"]
    while True:
        estado = input(msg_input).strip().lower()
        if not estado:
            print(msg_error_vacio)
            continue
        if estado in estados_permitidos:
            return estado.capitalize()
        else:
            print(msg_error_estado_no_valido)


def validar_prioridad(
        msg_input: str, msg_error_vacio: str, msg_error_prioridad_no_valida: str
) -> str:
    """
    Función para verificar el prioridad de las tarea en formato correcto.
    Solo aceptará valores permitidos.

    Args:
        msg_input (str): Mensaje de input
        msg_error_vacio (str): Mensaje de error cadena vacia
        msg_error_estado_no_valido (str): Mensaje de error prioridad no valido

    Returns:
        str: Prioridad valido.
    """
    estados_permitidos = ["alta", "media", "baja"]
    while True:
        prioridad = input(msg_input).strip().lower()
        if not prioridad:
            print(msg_error_vacio)
            continue
        if prioridad in estados_permitidos:
            return prioridad.capitalize()
        else:
            print(msg_error_prioridad_no_valida)


def seleccionar_tarea_por_titulo(msg_input: str, msg_tarea_no_encontrada: str, lista_tareas: object) -> object:
    """
    Método para seleccionar una tarea por el titulo.

    Args:
        msg_input (str): Mensaje de input
        msg_tarea_no_encontrada (str): Mensaje de error tarea no encontrada
        lista_tareas (object): Objeto que contiene objetos tareas

    Returns:
        object: objeto tarea encontrada
    """
    titulo_buscado = input(msg_input).strip().lower()
    for tarea in lista_tareas:
        if tarea.titulo.lower() == titulo_buscado:
            return tarea
    print(f"❌ {msg_tarea_no_encontrada}")
    return None
