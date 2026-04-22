"""
Módulo Principal - Gestor de Notas

Punto de entrada de la aplicación que coordina la interfaz de usuario
con la lógica del gestor. Controla el flujo del programa y el menú principal.
"""
from note import Nota
from manager import GestorNotas
from utils import menu, validar_opcion, formatear_cadenas

# RUTA
RUTA_ARCHIVO = "notes_gestor_poo/data/mis_notas.json"

# CONSTANTES DE INPUTS
MSG_INPUT_OPCION = "Introduce una opción: "
MSG_INPUT_TITULO = "Introduce el titulo de la nota: "
MSG_INPUT_DESCRIPCION = "Introduce la descripción de la nota: \n"
MSG_INPUT_ELIMINAR = "Seleccione el indice de la nota a elimminar: "

# CONSTANTES DE ERROR
MSG_ERROR_OPCION = "🛑 ERROR. Opción no válida."
MSG_ERROR_CAMPO_VACIO = "🛑 ERROR. El campo no puede estar vacio."

# CONSTANTES DE INFO MENU
MSG_SALIDA = "👋 Saliendo del programa."

# CONSTANTES DE INFO OBJETO
MSG_CARGADO = "✅ Notas cargadas correctamente."
MSG_NUEVO_FICHERO = "🆕 No se encontró archivo. Creando base de datos nueva..."
MSG_CORRUPTO = "⚠️ El archivo está dañado. Se ha reiniciado la base de datos."
MSG_GUARDADO = "💾 ¡Cambios guardados en el disco!"
MSG_LISTAR = "--- 📑 TUS NOTAS ---"
MSG_VACIO = "📭 No hay ninguna nota guardada."
MSG_ELIMINADA = "🗑️ Nota eliminada con éxito."
MSG_ERROR_ELIMINAR = "❌ Error: El número de nota no existe."


def main():
    """
    Función orquestadora del programa
    """
    notas = GestorNotas(
        RUTA_ARCHIVO, MSG_CARGADO, MSG_NUEVO_FICHERO, MSG_CORRUPTO,
        MSG_GUARDADO, MSG_LISTAR, MSG_VACIO, MSG_ELIMINADA,
        MSG_ERROR_ELIMINAR
    )
    while True:
        menu()
        opcion = validar_opcion(MSG_INPUT_OPCION, MSG_ERROR_OPCION)
        match opcion:
            case 1:
                titulo = formatear_cadenas(
                    MSG_INPUT_TITULO, MSG_ERROR_CAMPO_VACIO)
                descripcion = formatear_cadenas(
                    MSG_INPUT_DESCRIPCION, MSG_ERROR_CAMPO_VACIO)
                nota = Nota(titulo, descripcion)
                notas.add_nota(nota)
            case 2:
                notas.listar_notas()
            case 3:
                notas.listar_notas()
                indice_nota_a_eliminar = validar_opcion(
                    MSG_INPUT_ELIMINAR, MSG_ERROR_OPCION)
                notas.eliminar_nota(indice_nota_a_eliminar)
            case 4:
                print(MSG_SALIDA)
                break
            case _:
                print(MSG_ERROR_OPCION)


if __name__ == "__main__":
    main()
