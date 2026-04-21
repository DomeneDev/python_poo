
# 🔐 Password Generator

![Status](https://img.shields.io/badge/Status-Finalizado-success)
![Python](https://img.shields.io/badge/Python-3.10+-blue)

Un generador de contraseñas robusto diseñado bajo el principio de la **Navaja de Ockham**: la solución más sencilla suele ser la más eficaz. Este proyecto utiliza Programación Orientada a Objetos (POO) y una arquitectura modular para ofrecer una herramienta segura y fácil de mantener.

## 🚀 Características

- **Generación Multinivel:** 3 niveles de complejidad (Solo números, Alfanumérico y Completo).
- **Control de Longitud:** Rango de seguridad estandarizado entre 8 y 50 caracteres.
- **Auditoría en Tiempo Real:** Evaluación de seguridad basada en puntos de entropía (Baja, Media, Alta).
- **Interfaz Limpia:** Menú interactivo por consola con validación de errores.

## 🏗️ Arquitectura del Proyecto

El sistema se divide en cuatro módulos independientes para garantizar la escalabilidad:

1.  **`main.py` (El Orquestador):** Gestiona el bucle principal de la aplicación, el menú y la comunicación entre los distintos módulos.
2.  **`generator.py` (El Cerebro):** Clase `Generador` que utiliza un diccionario interno para mapear niveles de seguridad sin condicionales innecesarios.
3.  **`validator.py` (El Auditor):** Función analítica que utiliza *comprensiones de listas* y el método `any()` para verificar la presencia de diversos tipos de caracteres.
4.  **`utils.py` (Herramientas):** Funciones auxiliares para la limpieza de entradas de usuario y visualización de menús.

## 🛠️ Lógica de Seguridad

El sistema evalúa la fortaleza de cada contraseña mediante un sistema de puntos:
- **+1 Punto:** Longitud superior a 12 caracteres.
- **+1 Punto:** Presencia de números.
- **+1 Punto:** Presencia de mayúsculas.
- **+1 Punto:** Presencia de caracteres especiales (`string.punctuation`).
