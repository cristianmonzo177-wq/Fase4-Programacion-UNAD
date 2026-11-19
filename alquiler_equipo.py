
# UNAD - Programacion 213023
# Fase 4 - Sistema Software FJ

from servicio import Servicio
from excepciones import (
    ServicioNoDisponibleError,
    CalculoInvalidoError
)
from registro_logs import registrar_error


class AlquilerEquipo(Servicio):

    def __init__(self, codigo, nombre, precio_base, tipo_equipo):
        super().__init__(codigo, nombre, precio_base)

        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise ValueError(
                "El tipo de equipo es obligatorio."
            )

        self._tipo_equipo = tipo_equipo

    def validar_parametros(self, duracion):
        if isinstance(duracion, bool) or not isinstance(
            duracion, (int, float)
        ) or duracion <= 0:
            raise CalculoInvalidoError(
                "La duracion debe ser mayor que cero."
            )

        if not self.esta_disponible():
            raise ServicioNoDisponibleError(
                "El equipo no esta disponible."
            )

    def calcular_costo(self, duracion):
        try:
            self.validar_parametros(duracion)
            costo = self._precio_base * duracion

            if costo <= 0:
                raise CalculoInvalidoError(
                    "El costo calculado no es valido."
                )

            return costo

        except (
            CalculoInvalidoError,
            ServicioNoDisponibleError
        ) as error:
            registrar_error(
                f"Error al calcular alquiler de equipo: {error}"
            )
            raise

    def describir_servicio(self):
        return (
            f"Servicio: {self._nombre}\n"
            f"Codigo: {self._codigo}\n"
            f"Tipo de equipo: {self._tipo_equipo}\n"
            f"Precio por hora: ${self._precio_base:,.0f}"
        )
