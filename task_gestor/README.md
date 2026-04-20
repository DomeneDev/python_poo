# ✍ Gestor de Tareas 2.0 (POO Edition)

Sistema integral de gestión de tareas desarrollado en **Python** bajo el paradigma de **Programación Orientada a Objetos (POO)**. Este proyecto demuestra la implementación de una arquitectura modular, encapsulación de datos y validaciones robustas.

---

## 🚀 Características Principales

- **Paradigma POO:** Uso de clases y métodos de instancia para un código mantenible y escalable.
- **Validación Robusta:** Control de errores mediante bloques `try/except` y validaciones de "lista blanca" para estados y prioridades.
- **Búsqueda Inteligente:** Localización de tareas por título para facilitar operaciones de actualización y borrado.
- **Visualización Pro:** Representación visual dinámica mediante emojis según la prioridad (🔴 Alta, 🟡 Media, 🔵 Baja).
- **Encapsulación:** Atributos protegidos y métodos específicos (`obtener_tareas()`) para gestionar el acceso a los datos.

---

## 🛠️ Arquitectura del Proyecto

El proyecto se divide en cuatro módulos principales para garantizar la separación de responsabilidades:

1.  **`models.py`**: Define la clase `Tarea`. Gestiona el estado interno, el formateo de prioridades y la representación visual (`__str__`).
2.  **`task_manager.py`**: El motor del sistema (`GestorTareas`). Gestiona la colección de objetos, permitiendo añadir, listar, filtrar y eliminar tareas.
3.  **`utils.py`**: Biblioteca de soporte para la interacción con el usuario, incluyendo menús de consola y validadores de entrada.
4.  **`main.py`**: Orquestador principal que implementa el bucle de ejecución y el control de flujo mediante `match/case`.

---
