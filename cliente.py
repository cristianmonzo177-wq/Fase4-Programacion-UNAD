
# Clase Cliente
# Sistema de Gestion Software FJ
# UNAD - Programacion - Fase 4

class Cliente:
    # Constructor de la clase Cliente
    def __init__(self, nombre, documento, correo):
        self.nombre = nombre
        self.__documento = documento
        self.__correo = correo

        # Validar los datos al crear el cliente
        self.validar_datos()

    # Metodo para validar los datos personales
    def validar_datos(self):
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ValueError("El nombre no puede estar vacio.")

        if not isinstance(self.__documento, str) or not self.__documento.isdigit():
            raise ValueError("El documento debe contener solo numeros.")

        if not isinstance(self.__correo, str) or "@" not in self.__correo:
            raise ValueError("El correo electronico no es valido.")

    # Metodo para obtener el documento
    def obtener_documento(self):
        return self.__documento

    # Metodo para obtener el correo
    def obtener_correo(self):
        return self.__correo

    # Metodo para mostrar informacion del cliente
    def mostrar_informacion(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Documento: {self.__documento}\n"
            f"Correo: {self.__correo}"
        )
