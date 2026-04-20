"""
Archivo principal del Gestor de Tareas.
Este módulo orquestra la interacción entre el usuario, el gestor y las utilidades.
"""

from models import Tarea
from task_manager import GestorTareas
from utils import menu, validar_opcion, formatear_cadenas, validar_estado, validar_prioridad, seleccionar_tarea_por_titulo

# Constantes de mensajes de inputs
MSG_INPUT_OPCION = "Selecciones una opción: "
MSG_INPUT_TITULO = "Titulo de la tarea: "
MSG_INPUT_DESCRIPCION = "Descripción de la tarea: "
MSG_INPUT_PRIORIDAD = "Prioridad de la tarea (Alta/Media/Baja): "
MSG_INPUT_SELECCIONAR_TAREA_ACTUALIZAR = "Titulo de la tarea a actualizar: "
MSG_INPUT_SELECCIONAR_TAREA_ELIMINAR = "Titulo de la tarea a eliminar: "
MSG_INPUT_ESTADO = "Indique el nuevo estado de la tarea (En curso/Finalizada): "
MSG_INPUT_FILTRO = "¿Quieres filtrar tareas por estado (S/N)?: "
MSG_INPUT_FILTRO_TAREA = "Introduce el filtro de estado (Pendiente/En curso/Finalizada): "

# Constantes de mensajes de error
MSG_ERROR_OPCION = "🛑 ERROR: Opción no válida"
MSG_ERROR_TITULO_VACIO = "🛑 ERROR: El titulo no puede estar vacio."
MSG_ERROR_DESCRIPCION_VACIO = "🛑 ERROR: La descripción no puede estar vacia."
MSG_ERROR_PRIORIDAD_VACIO = "🛑 ERROR: La prioridad no puede estar vacia"
MSG_ERROR_PRIORIDAD_NO_VALIDA = "🛑 ERROR: La prioridad debe ser (Alta/Media/Baja)."
MSG_ERROR_TAREA_NO_ENCONTRADA = "🤷‍♂️ La tarea indicada no existe...."
MSG_ERROR_ESTADO_VACIO = "🛑 ERROR: El estado no puede estar vacio."
MSG_ERROR_ESTADO_NO_VALIDO = "🛑 ERROR: El estado tiene que ser un estado válido."


# Constantes de mensajes de información
MSG_INFO_TAREA_ADD = "📝 Tarea añadida."
MSG_INFO_TAREA_ACTUALIZADA = "✅ Tarea acualizada"
MSG_INFO_CONFIRMAR_ELIMINACION = "¿Está seguro que quiere eliminar la tarea (S/N)?: "
MSG_INFO_TAREA_ELIMINADA = "❌ Tarea eliminada"
MSG_INFO_OPERACION_CANCELADA = "Operación cancelada"
MSG_INFO_TAREAS_ESTADO = "Listado de tareas en estado: "
MSG_INFO_TAREAS_SIN_FILTRO = "Listado de tareas: "

# Constantes de comparación de valores
VALORES_PERMITIDOS_EN_ESTADOS = ["Pendiente", "En curso", "Finalizada"]


def main():
    mi_gestor_de_tareas = GestorTareas()
    while True:
        menu()
        opcion = validar_opcion(MSG_INPUT_OPCION, MSG_ERROR_OPCION)
        match opcion:
            case 1:
                titulo = formatear_cadenas(
                    MSG_INPUT_TITULO, MSG_ERROR_TITULO_VACIO)
                descripcion = formatear_cadenas(
                    MSG_INPUT_DESCRIPCION, MSG_ERROR_DESCRIPCION_VACIO)
                prioridad = validar_prioridad(
                    MSG_INPUT_PRIORIDAD, MSG_ERROR_PRIORIDAD_VACIO, MSG_ERROR_PRIORIDAD_NO_VALIDA
                )
                tarea = Tarea(titulo, descripcion, prioridad)
                mi_gestor_de_tareas.add_tarea(tarea)
                print(MSG_INFO_TAREA_ADD)
            case 2:
                tarea_a_actualizar = seleccionar_tarea_por_titulo(
                    MSG_INPUT_SELECCIONAR_TAREA_ACTUALIZAR, MSG_ERROR_TAREA_NO_ENCONTRADA,
                    mi_gestor_de_tareas.obtener_tareas()
                )
                nuevo_estado = validar_estado(
                    MSG_INPUT_ESTADO, MSG_ERROR_ESTADO_VACIO, MSG_ERROR_ESTADO_NO_VALIDO
                )
                tarea_a_actualizar.actualizar_estado(nuevo_estado)
                print(f"{tarea_a_actualizar} \n" + MSG_INFO_TAREA_ACTUALIZADA)
            case 3:
                tarea_a_eliminar = seleccionar_tarea_por_titulo(
                    MSG_INPUT_SELECCIONAR_TAREA_ELIMINAR, MSG_ERROR_TAREA_NO_ENCONTRADA,
                    mi_gestor_de_tareas.obtener_tareas()
                )
                print(tarea_a_eliminar)
                eliminar = input(MSG_INFO_CONFIRMAR_ELIMINACION).upper()
                if eliminar == "S":
                    indice_real = mi_gestor_de_tareas.obtener_tareas().index(
                        tarea_a_eliminar) + 1
                    mi_gestor_de_tareas.eliminar_tarea(indice_real)
                    print(MSG_INFO_TAREA_ELIMINADA)
                elif eliminar == "N":
                    print(MSG_INFO_OPERACION_CANCELADA)
                else:
                    print(MSG_INFO_OPERACION_CANCELADA)
            case 4:
                while True:
                    filtro = input(MSG_INPUT_FILTRO).upper()
                    match filtro:
                        case "S":
                            while True:
                                filtro_tarea = input(
                                    MSG_INPUT_FILTRO_TAREA).capitalize()
                                if filtro_tarea in VALORES_PERMITIDOS_EN_ESTADOS:
                                    print(MSG_INFO_TAREAS_ESTADO +
                                          f"{filtro_tarea}")
                                    mi_gestor_de_tareas.listar_tareas(
                                        filtro_tarea)
                                    break
                                else:
                                    print(MSG_ERROR_ESTADO_NO_VALIDO)
                        case "N":
                            print(MSG_INFO_TAREAS_SIN_FILTRO)
                            mi_gestor_de_tareas.listar_tareas()
                            break
                        case _:
                            print(MSG_ERROR_OPCION)
            case _:
                pass


if __name__ == "__main__":
    main()
