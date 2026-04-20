"""
Módulo de lógica de negocio para el Gestor de Tareas.

Este módulo gestiona la colección de objetos Tarea, permitiendo su
almacenamiento, filtrado y actualización de estado.
"""


class GestorTareas:
    """
    Controlador principal que gestiona el ciclo de vida de las tareas.
    """

    def __init__(self):
        """
        Inicializa el gestor con una lista privada de tareas.
        """
        self._tareas = []

    def add_tarea(self, tarea: object):
        """
        Recibe un objeto Tarea y lo guarda en la colección.

        Args:
            tarea (object): Instancia de la clase Tarea.
        """
        self._tareas.append(tarea)

    def obtener_tareas(self):
        """
        Devolver lista de tareas privada para utilización fuera del objeto

        Returns:
            Lista de tareas
        """
        return self._tareas

    def listar_tareas(self, filtro_estado: str = None):
        """
        Muestra las tareas por pantalla. Permite filtrar por estado.

        Args:
            filtro_estado (str, optional): Estado por el cual filtrar
            (Pendiente, En curso, Completada). Si es None, muestra todas.
        """
        for i, tarea in enumerate(self._tareas, start=1):
            if filtro_estado is None:
                print(f"{i}.- {tarea}")
            elif filtro_estado == tarea.estado:
                print(f"{i}.- {tarea}")

    def actualizar_estado_tarea(self, indice: int, nuevo_estado: str):
        """
        Modifica el estado de una tarea específica según su índice.

        Args:
            indice (int): Posición de la tarea en la lista (formato humano 1..N).
            nuevo_estado (str): El nuevo estado a asignar.
        """
        posicion = indice - 1
        if 0 <= posicion < len(self._tareas):
            tarea = self._tareas[posicion]
            tarea.actualizar_estado(nuevo_estado)
            print(f"✅ Tarea {indice} actualizada correctamente.")
        else:
            print(f"❌ Error: La tarea {indice} no existe.")

    def eliminar_tarea(self, indice: int):
        """
        Elimina una tarea de la lista según su posición (formato humano 1..N).

        Args:
            indice (int): Posición de la tarea en la lista.
        """
        posicion = indice - 1
        if 0 <= posicion < len(self._tareas):
            self._tareas.pop(posicion)
            print(f"✅ Tarea {indice} eliminada correctamente.")
        else:
            print(f"❌ Error: La tarea {indice} no existe.")
