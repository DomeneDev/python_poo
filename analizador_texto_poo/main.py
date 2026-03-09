"""
Punto de Entrada - Analizador de Texto POO

Este script es el orquestador principal del programa. Se encarga de
la interacción con el usuario, la instanciación de los objetos necesarios
y la presentación de los resultados finales.

Uso:
    Ejecutar directamente para iniciar la interfaz de línea de comandos.
"""

from analizador import MotorAnalizador


def main():
    """
    Función principal de programa de analizador de texto
    """
    texto = input("Introduce el texto a analizar: \n")
    resultados_analizador_de_texto = MotorAnalizador(texto)
    resultados = resultados_analizador_de_texto.ejecutar()
    print(resultados)


if __name__ == "__main__":
    main()
