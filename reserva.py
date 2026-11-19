
# UNAD - Programacion 213023
# Fase 4 - Sistema Software FJ
# Clase Reserva

from cliente import Cliente
from servicio import Servicio


class Reserva:

    def __init__(self, codigo, cliente, servicio, duracion):

        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El codigo de reserva es obligatorio.")

        if not isinstance(cliente, Cliente):
            raise TypeError("Debe proporcionar un cliente valido.")

        if not isinstance(servicio, Servicio):
            raise TypeError("Debe proporcionar un servicio valido.")

        if isinstance(duracion, bool) or not isinstance(
            duracion, (int, float)
        ) or duracion <= 0:
            raise ValueError("La duracion debe ser mayor que cero.")

        self.__codigo = codigo
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

    def confirmar(self):
        if self.__estado != "Pendiente":
            raise ValueError("Solo se pueden confirmar reservas pendientes.")

        self.__servicio.validar_parametros(self.__duracion)
        self.__estado = "Confirmada"

        return "Reserva confirmada correctamente."

    def cancelar(self):
        if self.__estado == "Cancelada":
            raise ValueError("La reserva ya fue cancelada.")

        self.__estado = "Cancelada"
        return "Reserva cancelada correctamente."

    def procesar(self):
        try:
            if self.__estado != "Confirmada":
                raise ValueError("La reserva debe estar confirmada.")

            costo = self.__servicio.calcular_costo(
                self.__duracion
            )

        except (ValueError, TypeError) as error:
            return f"Error al procesar reserva: {error}"

        else:
            return (
                f"Reserva: {self.__codigo}\n"
                f"Cliente: {self.__cliente.obtener_nombre()}\n"
                f"Estado: {self.__estado}\n"
                f"Costo total: ${costo:,.0f}"
            )

    def obtener_estado(self):
        return self.__estado
