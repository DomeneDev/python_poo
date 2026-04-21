"""
Módulo Principal - Generador de Contraseñas Pro

Este archivo actúa como el orquestador del sistema. Se encarga de la
interacción directa con el usuario, la gestión del flujo del programa
y la presentación de los resultados finales.
"""
from generator import Generador
from validator import evaluar_seguridad
from utils import menu, validar_opcion, validar_nivel, establecer_longitud

# CONSTANTES PARA MSG DE INPUTS
MSG_INPUT_OPCION = "Introduzca una opción: "
MSG_INPUT_NIVEL = "Introduzca el nivel de la contraseña: "
MSG_INPUT_LONGITUD = " Introduzca la longitud de la contraseña (min 8, max 50): "

# CONSTANTES PARA MSG DE ERROR
MSG_ERROR_OPCION = "🛑 ERROR: Opción no válida"

# CONSTANTES PARA MSG DE INFORMACIÓN
MSG_PASS_GENERADA = "Contraseña generada: "
MSG_EXIT = " 🖐 Saliendo del programa... hasta la proxima"


def main():
    """
    Función principal de la app, orquestador
    """
    password = Generador()
    while True:
        menu()
        opcion = validar_opcion(MSG_INPUT_OPCION, MSG_ERROR_OPCION)
        match opcion:
            case 1:
                nivel = validar_nivel(MSG_INPUT_NIVEL, MSG_ERROR_OPCION)
                longitud = establecer_longitud(
                    MSG_INPUT_LONGITUD, MSG_ERROR_OPCION)
                password_generada = password.generar(nivel, longitud)
                print(MSG_PASS_GENERADA)
                print(password_generada)
                print(
                    f"Nivel de seguridad: {evaluar_seguridad(password_generada)}")
            case 2:
                print(MSG_EXIT)
                break
            case _:
                print(MSG_ERROR_OPCION)


if __name__ == "__main__":
    main()
