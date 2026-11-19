
# Universidad Nacional Abierta y a Distancia
# Curso: Programacion 213023
# Fase 4 - Practicas simuladas

# Importar la clase abstracta Entidad
from entidad import Entidad


# Clase Cliente que hereda de Entidad
class Cliente(Entidad):

    # Constructor de la clase Cliente
    def __init__(self, nombre, documento, correo):

        # Inicializar la clase padre
        super().__init__(documento)

        # Encapsular los datos personales
        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo

        # Validar los datos ingresados
        self.validar_datos()

    # Metodo para validar los datos del cliente
    def validar_datos(self):

        if not isinstance(self.__nombre, str) or not self.__nombre.strip():
            raise ValueError("El nombre no puede estar vacio.")

        if not isinstance(self.__documento, str) or not self.__documento.isdigit():
            raise ValueError("El documento debe contener solo numeros.")

        if not isinstance(self.__correo, str) or "@" not in self.__correo:
            raise ValueError("El correo electronico no es valido.")

    # Metodo para obtener el nombre
    def obtener_nombre(self):
        return self.__nombre

    # Metodo para obtener el documento
    def obtener_documento(self):
        return self.__documento

    # Metodo para obtener el correo
    def obtener_correo(self):
        return self.__correo

    # Implementacion del metodo abstracto
    def mostrar_informacion(self):
        return (
            f"Nombre: {self.__nombre}\n"
            f"Documento: {self.__documento}\n"
            f"Correo: {self.__correo}"
        )
        
