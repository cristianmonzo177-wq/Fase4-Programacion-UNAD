
# Universidad Nacional Abierta y a Distancia
# Curso: Programacion 213023
# Fase 4 - Practicas simuladas
# Clase abstracta Entidad

# Importar las herramientas para crear clases abstractas
from abc import ABC, abstractmethod


# Clase abstracta que representa una entidad general
class Entidad(ABC):

    # Constructor de la clase
    def __init__(self, identificador):
        self._identificador = identificador

    # Metodo para obtener el identificador
    def obtener_identificador(self):
        return self._identificador

    # Metodo abstracto que deben implementar las clases hijas
    @abstractmethod
    def mostrar_informacion(self):
        pass
