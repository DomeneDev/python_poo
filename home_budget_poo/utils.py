"""
Modulo para apoyo de main
"""


def mostrar_menu():
    """
    Menú para seleccionar opciones
    """
    print("+---------------------+")
    print("| Home budget 2.0  🏡 |")
    print("+---------------------+")
    print("| 1- Añadir movimiento|")
    print("| 2- Mostrar informe  |")
    print("| 3- Salir            |")
    print("+---------------------+")


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


def leer_cadenas(msg_input: str, msg_error: str) -> str:
    """
    Función para verificar el texto de las cadenas en formato correcto.
    Lo vamos a pasar en minúsculas al constructor, ya que este tiene un
    método propio para dar su propio formato.

    Args:
        msg_input (str): Mensaje de input
        msg_error (str): Mensaje de error

    Returns:
        str: Texto conformato correcto.
    """
    while True:
        texto = input(msg_input).lower()
        try:
            if not texto.strip():
                raise ValueError(msg_error)
        except ValueError as e:
            print((f"❌ ERROR: {e}"))
        else:
            break
    return texto


def validar_tipo_movimiento(msg_input: str, msg_error: str) -> str:
    """
    Función para validar el tipo de movimiento
    Valores posibles
    - gasto
    - ingreso
    Vamos a pasarlo en minusculas al constructor, ya que este tiene un
    método propio para dar su propio formato

    Args:
        msg_input (str): Mensaje de input
        msg_error (str): Mensaje de error

    Returns:
        str: Tipo de movimiento con valor correcto
    """
    while True:
        tipo = input(msg_input).lower()
        if tipo == "ingreso":
            return tipo
        elif tipo == "gasto":
            return tipo
        else:
            print(f"❌ ERROR: {msg_error}")


def validacion_dato(msg_input: str, msg_error: str, tipo_dato: type):
    """
    Función para validar datos

    Args:
        msg_input (str): Mensaje de input
        msg_error_neg (str): Mensaje de error, precio negativo.
        msg_error (str): Mensaje de error generico
        tipo_dato (_type_): Tipo de dato esperado.

    Returns:
        float: Dato con formato correcto de moneda
    """
    while True:
        dato = input(msg_input)
        try:
            dato = tipo_dato(dato)
            break
        except ValueError:
            print(f"❌ ERROR: {msg_error}")
    return dato
