# 🏡 Home Budget 2.0: Gestión Financiera Pro

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![POO](https://img.shields.io/badge/Paradigm-OOP-green?style=for-the-badge)
![Clean Code](https://img.shields.io/badge/Code_Style-Solid-orange?style=for-the-badge)

Segunda etapa de mi laboratorio de Python, donde evolucionamos un gestor de gastos básico a una **Arquitectura Orientada a Objetos** robusta, modular y con validación de datos en tiempo real.

## 🚀 Características Principales
- **Validación Robusta:** Sistema anti-errores en la entrada de datos (cantidades numéricas y tipos de movimiento).
- **Sanitización Automática:** Los objetos "limpian" sus propios datos (espacios, mayúsculas, valores negativos).
- **Informe Visual:** Historial detallado con indicadores visuales (🟢/🔴) y balance neto calculado automáticamente.
- **Arquitectura Multicapa:** Separación clara entre modelos, lógica de negocio y utilidades.

## 🏗️ Estructura del Proyecto
El código se divide en 4 módulos estratégicos:

* **`models.py`**: Define la entidad `Movimiento`. Contiene la lógica de auto-validación y el formato de impresión (`__str__`).
* **`gestor.py`**: El cerebro del sistema (`CalculadoraPresupuesto`). Gestiona la colección de objetos y los cálculos matemáticos.
* **`utils.py`**: Capa de soporte encargada de la interacción limpia con el usuario y captura de excepciones.
* **`main.py`**: El orquestador que inicia el programa y mantiene el estado de la aplicación.

