
# UNAD - Programacion 213023
# Fase 4 - Sistema Software FJ

from entidad import Entidad


class Cliente(Entidad):

    def __init__(self, nombre, documento, correo):
        super().__init__(documento)

        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo

        self.validar_datos()

    def validar_datos(self):
        if not isinstance(self.__nombre, str) or not self.__nombre.strip():
            raise ValueError("El nombre no puede estar vacio.")

        if not isinstance(self.__documento, str) or not self.__documento.isdigit():
            raise ValueError("El documento debe contener solo numeros.")

        if not isinstance(self.__correo, str) or "@" not in self.__correo:
            raise ValueError("El correo electronico no es valido.")

    def obtener_nombre(self):
        return self.__nombre

    def obtener_documento(self):
        return self.__documento

    def obtener_correo(self):
        return self.__correo

    def mostrar_informacion(self):
        return (
            f"Nombre: {self.__nombre}\n"
            f"Documento: {self.__documento}\n"
            f"Correo: {self.__correo}"
        )
