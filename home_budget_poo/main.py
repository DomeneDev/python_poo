"""
Main de la aplicación, Se encarga de la interacción con el usuario, la
instanaciación de los objetos necesarios y la represantaicón de los
resultados
"""

from models import Movimiento
from gestor import CalculadoraPresupuesto
from utils import mostrar_menu, validar_opcion, leer_cadenas, validar_tipo_movimiento, validacion_dato


# Constantes de MSG_INPUTS
MSG_INPUT_OPCION = "Seleccione una opción: "
MSG_INPUT_CONCEPTO = "Introduzca concepto: "
MSG_INPUT_CANTIDAD = "Introduzca la cantidad: "
MSG_INPUT_CATEGORIA = "Introduzca la categoria: "
MSG_INPUT_TIPO = "Introduzca el tipo de movimiento (Gasto/Ingreso): "

# Constantes de MSG_ERRORS
MSG_ERROR_OPCION = "ERROR: Debe introducir el valor numérico de la opción."
MSG_ERROR_CONCEPTO = "ERROR: No has introducido un concepto válido."
MSG_ERROR_CANTIDAD = "ERROR: La cantidad debe ser un valor numérico."
MSG_ERROR_CATEGORIA = "ERROR: La categoria no es válida."
MSG_ERROR_TIPO = "ERROR: Tipo de movimiento no válido."

# Constantes para mensajes génericos
MSG_MOVIMIENTO_ANOTADO = "🖊 Movimiento anotado..."
MSG_SALIDA = "Cerrando programa...👋...¡Hasta pronto!"


def main():
    """
    Función principal de programa de home_bugdet.
    """
    mi_gestor = CalculadoraPresupuesto()
    while True:
        mostrar_menu()
        opcion = validar_opcion(MSG_INPUT_OPCION, MSG_ERROR_OPCION)
        match opcion:
            case 1:
                concepto = leer_cadenas(MSG_INPUT_CONCEPTO, MSG_ERROR_CONCEPTO)
                cantidad = validacion_dato(
                    MSG_INPUT_CANTIDAD, MSG_ERROR_CANTIDAD, float)
                categoria = leer_cadenas(
                    MSG_INPUT_CATEGORIA, MSG_ERROR_CATEGORIA)
                tipo = validar_tipo_movimiento(MSG_INPUT_TIPO, MSG_ERROR_TIPO)
                mov = Movimiento(concepto, cantidad, categoria, tipo)
                mi_gestor.registrar_movimiento(mov)
                print(MSG_MOVIMIENTO_ANOTADO)
            case 2:
                mi_gestor.generar_informe()
            case 3:
                print(MSG_SALIDA)
                break


if __name__ == "__main__":
    main()
