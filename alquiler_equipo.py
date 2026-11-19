
# UNAD - Programacion 213023
# Fase 4 - Sistema Software FJ
# Servicio especializado: Alquiler de equipos

from servicio import Servicio


class AlquilerEquipo(Servicio):

    def __init__(self, codigo, nombre, precio_base, tipo_equipo):
        super().__init__(codigo, nombre, precio_base)

        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise ValueError("El tipo de equipo es obligatorio.")

        self._tipo_equipo = tipo_equipo

    def validar_parametros(self, duracion):
        if isinstance(duracion, bool) or not isinstance(
            duracion, (int, float)
        ) or duracion <= 0:
            raise ValueError("La duracion debe ser mayor que cero.")

        if not self.esta_disponible():
            raise ValueError("El equipo no esta disponible.")

    def calcular_costo(self, duracion):
        self.validar_parametros(duracion)
        return self._precio_base * duracion

    def describir_servicio(self):
        return (
            f"Servicio: {self._nombre}\n"
            f"Codigo: {self._codigo}\n"
            f"Tipo de equipo: {self._tipo_equipo}\n"
            f"Precio por hora: ${self._precio_base:,.0f}"
        )
