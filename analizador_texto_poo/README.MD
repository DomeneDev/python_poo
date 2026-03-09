# 🚀 Analizador de Texto Inteligente (POO Edition)

Este proyecto marca el inicio de mi **Evolución 2.0** como desarrollador. Representa la transición de una programación funcional/procedimental hacia la **Programación Orientada a Objetos (POO)**, aplicando conceptos de encapsulamiento y modularidad.

---

## 🎯 Objetivo del Proyecto
Transformar un procesador de texto convencional en un sistema robusto donde la lógica y los datos coexisten en entidades independientes (objetos). 

### 💡 Evolución del Código
- **v1.0 (Procedimental):** Funciones aisladas que recibían y devolvían strings/números.
- **v2.0 (POO):** Uso de clases "Motor" para procesar y clases "Modelo" para estructurar resultados.

---

## 🏗️ Arquitectura del Sistema

El proyecto se divide en tres pilares fundamentales:

1. **`models.py`**: Define la clase `ResultadosAnalisis`. Es el contenedor inteligente que almacena las métricas y sabe cómo representarse a sí mismo.
2. **`analizador.py`**: Contiene la clase `MotorAnalizador`. Es el cerebro del sistema que encapsula el comportamiento del análisis.
3. **`main.py`**: El orquestador que gestiona la entrada del usuario e instancia los objetos.

---

## 🚀 Funcionalidades Actuales
- ✅ **Encapsulamiento de Texto**: Limpieza automática de espacios al instanciar.
- ✅ **Métricas en Tiempo Real**: Conteo preciso de palabras y caracteres.
- ✅ **Generación de Objetos**: El motor no devuelve texto, devuelve una instancia de resultado.
- ✅ **Informes Estructurados**: Visualización profesional mediante el método mágico `__str__`.
