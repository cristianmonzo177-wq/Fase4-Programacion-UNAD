
# UNAD - Programacion 213023
# Fase 4 - Sistema Software FJ
# Clase Reserva con excepciones y logs

from cliente import Cliente
from servicio import Servicio

from excepciones import (
    ReservaInvalidaError,
    ServicioNoDisponibleError,
    OperacionNoPermitidaError,
    CalculoInvalidoError
)

from registro_logs import registrar_evento, registrar_error


class Reserva:

    def __init__(self, codigo, cliente, servicio, duracion):

        if not isinstance(codigo, str) or not codigo.strip():
            raise ReservaInvalidaError(
                "El codigo de reserva es obligatorio."
            )

        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError(
                "Debe proporcionar un cliente valido."
            )

        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError(
                "Debe proporcionar un servicio valido."
            )

        if isinstance(duracion, bool) or not isinstance(
            duracion, (int, float)
        ) or duracion <= 0:
            raise ReservaInvalidaError(
                "La duracion debe ser mayor que cero."
            )

        self.__codigo = codigo
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

        registrar_evento(
            f"Reserva {self.__codigo} creada correctamente."
        )

    def confirmar(self):
        try:
            if self.__estado != "Pendiente":
                raise OperacionNoPermitidaError(
                    "Solo se pueden confirmar reservas pendientes."
                )

            if not self.__servicio.esta_disponible():
                raise ServicioNoDisponibleError(
                    "El servicio no esta disponible."
                )

            self.__servicio.validar_parametros(
                self.__duracion
            )

        except (
            OperacionNoPermitidaError,
            ServicioNoDisponibleError,
            CalculoInvalidoError,
            ValueError
        ) as error:

            registrar_error(
                f"Error al confirmar reserva: {error}"
            )
            raise

        else:
            self.__estado = "Confirmada"

            registrar_evento(
                f"Reserva {self.__codigo} confirmada."
            )

            return "Reserva confirmada correctamente."

    def cancelar(self):
        if self.__estado == "Cancelada":
            error = OperacionNoPermitidaError(
                "La reserva ya fue cancelada."
            )

            registrar_error(str(error))
            raise error

        self.__estado = "Cancelada"

        registrar_evento(
            f"Reserva {self.__codigo} cancelada."
        )

        return "Reserva cancelada correctamente."

    def procesar(self):
        try:
            if self.__estado != "Confirmada":
                raise ReservaInvalidaError(
                    "La reserva debe estar confirmada."
                )

            costo = self.__servicio.calcular_costo(
                self.__duracion
            )

            if (
                isinstance(costo, bool)
                or not isinstance(costo, (int, float))
                or costo <= 0
            ):
                raise CalculoInvalidoError(
                    "El costo calculado no es valido."
                )

        except (
            ReservaInvalidaError,
            CalculoInvalidoError,
            ServicioNoDisponibleError,
            ValueError
        ) as error:

            registrar_error(
                f"Error al procesar reserva: {error}"
            )

            return f"Error al procesar reserva: {error}"

        else:
            registrar_evento(
                f"Reserva {self.__codigo} procesada."
            )

            return (
                f"Reserva: {self.__codigo}\n"
                f"Cliente: {self.__cliente.obtener_nombre()}\n"
                f"Estado: {self.__estado}\n"
                f"Costo total: ${costo:,.0f}"
            )

        finally:
            registrar_evento(
                f"Finalizo procesamiento de reserva {self.__codigo}."
            )

    def obtener_estado(self):
        return self.__estado
