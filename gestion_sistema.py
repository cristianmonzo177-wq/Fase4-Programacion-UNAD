
# UNAD - Programacion 213023
# Fase 4 - Sistema Software FJ
# Gestion de listas internas

from cliente import Cliente
from servicio import Servicio
from reserva import Reserva


class GestionSistema:

    def __init__(self):
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

    def agregar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("Debe ingresar un cliente valido.")

        self.__clientes.append(cliente)
        return "Cliente agregado correctamente."

    def agregar_servicio(self, servicio):
        if not isinstance(servicio, Servicio):
            raise TypeError("Debe ingresar un servicio valido.")

        self.__servicios.append(servicio)
        return "Servicio agregado correctamente."

    def agregar_reserva(self, reserva):
        if not isinstance(reserva, Reserva):
            raise TypeError("Debe ingresar una reserva valida.")

        self.__reservas.append(reserva)
        return "Reserva agregada correctamente."

    def listar_clientes(self):
        return [
            cliente.mostrar_informacion()
            for cliente in self.__clientes
        ]

    def listar_servicios(self):
        return [
            servicio.describir_servicio()
            for servicio in self.__servicios
        ]

    def listar_reservas(self):
        return [
            reserva.obtener_estado()
            for reserva in self.__reservas
        ]

    def obtener_totales(self):
        return {
            "clientes": len(self.__clientes),
            "servicios": len(self.__servicios),
            "reservas": len(self.__reservas)
        }
