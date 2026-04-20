"""
Módulo de modelos para el Gestor de Tareas.

Este módulo define la entidad Tarea, encargada de representar las actividades
individuales, su prioridad, estado y metadatos asociados.
"""

from datetime import datetime


class Tarea:
    """
    Representa una tarea individual dentro del sistema.
    """

    def __init__(self, titulo: str, descripcion: str, prioridad: str):
        """
        Constructor de la clase Tarea.

        Args:
            titulo (str): Nombre o título de la tarea.
            descripcion (str): Detalle de la actividad a realizar.
            prioridad (str): Nivel de importancia (Alta, Media, Baja).
        """
        # Aquí irán tus atributos y llamadas a métodos de limpieza
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = self._formatear_prioridad(prioridad)
        self.estado = "Pendiente"
        self.fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def _formatear_prioridad(self, prioridad: str) -> str:
        """
        Valida y formatea la cadena de prioridad.

        Args:
            prioridad (str): Cadena de texto con la prioridad.

        Returns:
            str: Prioridad con la primera letra en mayúscula.
        """
        prioridad = prioridad.title().strip()
        if prioridad == "Alta":
            return "🔴 Alta"
        elif prioridad == "Media":
            return "🟡 Media"
        return "🔵 Baja"

    def actualizar_estado(self, nuevo_estado: str):
        """
        Modifica el estado actual de la tarea.

        Args:
            nuevo_estado (str): El nuevo estado (ej: 'En curso', 'Completada').
        """
        self.estado = nuevo_estado.capitalize()

    def __str__(self) -> str:
        """
        Genera una representación visual de la tarea incluyendo emojis por prioridad.

        Returns:
            str: Cadena formateada con el estado, prioridad y datos de la tarea.
        """
        return (
            f"[{self.estado}] {self.prioridad} | Titulo: {self.titulo}\n"
            f"📅 Creada: {self.fecha}\n"
            f"📝 Descripción: {self.descripcion}\n"
            f"{'-'*40}\n"
        )
