
# UNAD - Programacion 213023
# Fase 4 - Sistema Software FJ

from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, codigo, nombre, precio_base):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El codigo es obligatorio.")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre es obligatorio.")

        if (isinstance(precio_base, bool)
                or not isinstance(precio_base, (int, float))
                or precio_base <= 0):
            raise ValueError("El precio debe ser positivo.")

        self._codigo = codigo
        self._nombre = nombre
        self._precio_base = precio_base
        self._disponible = True

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass

    def esta_disponible(self):
        return self._disponible

    def cambiar_disponibilidad(self, disponible):
        if not isinstance(disponible, bool):
            raise ValueError(
                "La disponibilidad debe ser booleana."
            )
        self._disponible = disponible

    # Variante de calculo con impuesto y descuento
    def calcular_costo_total(
        self, duracion, impuesto=0, descuento=0
    ):
        if (isinstance(impuesto, bool)
                or not isinstance(impuesto, (int, float))
                or not 0 <= impuesto <= 100):
            raise ValueError(
                "El impuesto debe estar entre 0 y 100."
            )

        if (isinstance(descuento, bool)
                or not isinstance(descuento, (int, float))
                or not 0 <= descuento <= 100):
            raise ValueError(
                "El descuento debe estar entre 0 y 100."
            )

        subtotal = self.calcular_costo(duracion)
        total = subtotal * (1 - descuento / 100)
        total = total * (1 + impuesto / 100)

        return total
