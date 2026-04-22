# 🚀 Gestor de Notas Inteligente (POO Edition)

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Paradigm](https://img.shields.io/badge/paradigm-OOP-orange.svg)

Este proyecto representa la consolidación de conceptos de **Programación Orientada a Objetos (POO)**, aplicando una arquitectura de capas para separar la lógica de negocio, la persistencia de datos y la interfaz de usuario. Es el siguiente paso en mi **Evolución 2.0** como desarrollador.

---

## 🎯 Objetivo del Proyecto

Transformar un simple sistema de recordatorios en una aplicación robusta y escalable donde los datos (Notas) y la lógica (Gestor) coexisten en entidades independientes y persistentes.

## 💡 Evolución del Código

* **v1.0 (Persistencia)**: Implementación de guardado automático en formato JSON para evitar la pérdida de información entre sesiones.
* **v2.0 (Arquitectura Modular)**: División del sistema en módulos especializados para facilitar el mantenimiento y la legibilidad.

---

## 🏗️ Arquitectura del Sistema

El proyecto se divide en cuatro pilares fundamentales:

1. **`note.py`**: Define la clase `Nota`. Es la entidad que encapsula el título, la descripción y gestiona su propia marca de tiempo inteligente.
2. **`manager.py`**: Contiene la clase `GestorNotas`. Es el "motor" encargado de las operaciones CRUD y de sincronizar los objetos con el almacenamiento en disco.
3. **`utils.py`**: Módulo de herramientas auxiliares para la validación de tipos y el formateo estético de la interfaz.
4. **`main.py`**: El orquestador que gestiona el ciclo de vida de la aplicación e instancia los objetos necesarios.

---

## 🚀 Funcionalidades Actuales

* ✅ **Encapsulamiento de Datos**: Cada nota es un objeto autónomo que sabe cómo representarse a sí mismo mediante el método `__str__`.
* ✅ **Persistencia Automática**: Sincronización inmediata con `mis_notas.json` tras cada creación o eliminación.
* ✅ **Historial Cronológico**: El sistema diferencia entre notas nuevas y recuperadas, manteniendo la fecha original de creación.
* ✅ **Validación Robusta**: Tratamiento de errores para entradas vacías, tipos de datos incorrectos e índices fuera de rango.

---

## 📂 Estructura de Archivos

```text
notes_gestor_poo/
├── data/               # Directorio de persistencia
│   └── mis_notas.json  # Base de datos en formato JSON
├── note.py             # Clase Entidad
├── manager.py          # Clase Motor de Gestión
├── utils.py            # Herramientas de Interfaz
└── main.py             # Orquestador Principal
