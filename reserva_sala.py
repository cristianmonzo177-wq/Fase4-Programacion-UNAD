
# UNAD - Programacion 213023
# Fase 4 - Sistema Software FJ
# Servicio especializado: Reserva de salas

from servicio import Servicio


class ReservaSala(Servicio):

    def __init__(self, codigo, nombre, precio_base, capacidad):
        super().__init__(codigo, nombre, precio_base)

        if isinstance(capacidad, bool) or not isinstance(capacidad, int) or capacidad <= 0:
            raise ValueError("La capacidad debe ser un entero positivo.")

        self._capacidad = capacidad

    def validar_parametros(self, duracion):
        if isinstance(duracion, bool) or not isinstance(
            duracion, (int, float)
        ) or duracion <= 0:
            raise ValueError("La duracion debe ser mayor que cero.")

        if not self.esta_disponible():
            raise ValueError("La sala no esta disponible.")

    def calcular_costo(self, duracion):
        self.validar_parametros(duracion)
        return self._precio_base * duracion

    def describir_servicio(self):
        return (
            f"Servicio: {self._nombre}\n"
            f"Codigo: {self._codigo}\n"
            f"Capacidad: {self._capacidad} personas\n"
            f"Precio por hora: ${self._precio_base:,.0f}"
        )
