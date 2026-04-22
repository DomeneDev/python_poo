"""
Módulo de Gestión - El Administrador de Notas

Este módulo contiene la lógica para manipular la colección de notas.
Implementa las operaciones CRUD (Crear, Leer, Eliminar) y gestiona
la persistencia de datos en disco (formato JSON/TXT).
"""

# Importamos librerías necesarias json
import json

# Imporrtamos el modelo Note
from note import Nota


class GestorNotas():
    """
    Clase para gestionar las notas almacenadas en un archivo json
    """

    def __init__(
        self, ruta: str, msg_fichero_cargado: str, msg_nuevo_fichero: str,
        msg_fichero_corrupto: str, msg_notas_guardadas: str,
        msg_info_listar: str, msg_error_vacio: str,
        msg_info_eliminar: str, msg_error_eliminar: str
    ):
        """
        Constructor del objeto que contiene las notas
        """
        self.ruta = ruta
        self.msg_fichero_cargado = msg_fichero_cargado
        self.msg_nuevo_fichero = msg_nuevo_fichero
        self.msg_fichero_corrupto = msg_fichero_corrupto
        self.msg_notas_guardada = msg_notas_guardadas
        self.msg_info_listar = msg_info_listar
        self.msg_info_error_vacio = msg_error_vacio
        self.msg_info_eliminar = msg_info_eliminar
        self.msg_error_eliminar = msg_error_eliminar
        self.notas = self.cargar_notas()

    def cargar_notas(self) -> list:
        """
        Método para leer y cargar el archivo json de notas

        Args:
            ruta (str): Ruta donde se almacena el archivo
            msg_fichero_cargado (str): Mensaje de fichero cargada
            msg_nuevo_fichero (str): Mensaje de nuevo fichero
            msg_fichero_corrupto (str): Mensaje de fichero corrupto, se crea uno nuevo

        Returns:
            list: _description_
        """
        try:
            with open(self.ruta, 'r', encoding='utf-8')as f:
                notas_sin_procesar = json.load(f)
                print(self.msg_fichero_cargado)
                return [Nota(n['titulo'], n['descripcion'], n['fecha']) for n in notas_sin_procesar]
        except FileNotFoundError:
            notas = []
            print(self.msg_nuevo_fichero)
            return notas
        except json.JSONDecodeError:
            notas = []
            print(self.msg_fichero_corrupto)
            return notas

    def guardar_notas(self) -> str:
        """
        Método para guardar las notas dentro del objeto GestorNotas

        Returns:
            str: Mensaje de notas guardadas
        """
        notas_preparadas = [vars(nota) for nota in self.notas]
        with open(self.ruta, 'w', encoding='UTF-8') as f:
            json.dump(notas_preparadas, f, indent=4)
        print(self.msg_notas_guardada)

    def add_nota(self, nota: object):
        """
        Método para añadir una nota al objeto GestorNotas

        Args:
            nota (object): Nota a añadir
        """
        self.notas.append(nota)
        self.guardar_notas()

    def listar_notas(self) -> object:
        """
        Método para listar las notas

        Returns:
            object: objeto nota
        """
        if not self.notas:
            print(self.msg_info_error_vacio)
        else:
            print(self.msg_info_listar)
            for i, nota in enumerate(self.notas, start=1):
                print(f"{i} -  {nota}")

    def eliminar_nota(self, indice_nota_a_eliminar: int):
        """
        Método para elinimar una nota

        Args:
            indice_nota_a_eliminar (int): Indice de nota a eliminar
        """
        if not self.notas:
            print(self.msg_info_error_vacio)
        else:
            try:
                if 1 <= indice_nota_a_eliminar <= len(self.notas):
                    self.notas.pop(indice_nota_a_eliminar-1)
                    print(self.msg_info_eliminar)
                    self.guardar_notas()
            except IndexError:
                print(self.msg_error_eliminar)
