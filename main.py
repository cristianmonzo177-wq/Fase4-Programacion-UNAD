
# UNAD - Programacion 213023
# Fase 4 - Practicas simuladas
# Sistema Integral de Gestion - Software FJ

from cliente import Cliente
from reserva_sala import ReservaSala
from alquiler_equipo import AlquilerEquipo
from asesoria_especializada import AsesoriaEspecializada
from reserva import Reserva
from gestion_sistema import GestionSistema

from excepciones import ErrorSistema
from registro_logs import registrar_evento, registrar_error


def ejecutar_prueba(numero, descripcion, operacion):
    print(f"\nPRUEBA {numero}: {descripcion}")

    try:
        resultado = operacion()

    except (ErrorSistema, ValueError, TypeError) as error:
        print(f"Error controlado: {error}")
        registrar_error(f"Prueba {numero}: {error}")

    else:
        if resultado is not None:
            print(resultado)
        print("Operacion ejecutada.")

    finally:
        print(f"Fin de prueba {numero}.")


def main():
    print("=" * 50)
    print("BIENVENIDO A SOFTWARE FJ")
    print("Sistema de gestion de clientes y reservas")
    print("=" * 50)

    registrar_evento("Inicio del sistema Software FJ.")

    # Crear cliente y servicios
    cliente = Cliente(
        "Ana Martinez", "123456789", "ana@correo.com"
    )

    sala = ReservaSala(
        "S001", "Sala de reuniones", 50000, 20
    )

    equipo = AlquilerEquipo(
        "E001", "Proyector", 30000, "Audiovisual"
    )

    asesoria = AsesoriaEspecializada(
        "A001", "Asesoria tecnologica",
        80000, "Desarrollo de software"
    )

    # Crear reservas
    reserva1 = Reserva("R001", cliente, sala, 3)
    reserva2 = Reserva("R002", cliente, equipo, 4)
    reserva3 = Reserva("R003", cliente, asesoria, 2)

    # Pruebas originales
    ejecutar_prueba(
        1, "Consultar cliente",
        cliente.mostrar_informacion
    )

    ejecutar_prueba(
        2, "Consultar sala",
        sala.describir_servicio
    )

    ejecutar_prueba(
        3, "Calcular alquiler de equipo",
        lambda: equipo.calcular_costo(4)
    )

    ejecutar_prueba(
        4, "Calcular asesoria",
        lambda: asesoria.calcular_costo(2)
    )

    ejecutar_prueba(
        5, "Confirmar reserva de sala",
        reserva1.confirmar
    )

    ejecutar_prueba(
        6, "Procesar reserva de sala",
        reserva1.procesar
    )

    ejecutar_prueba(
        7, "Confirmar reserva de equipo",
        reserva2.confirmar
    )

    ejecutar_prueba(
        8, "Procesar reserva de equipo",
        reserva2.procesar
    )

    ejecutar_prueba(
        9, "Confirmar reserva de asesoria",
        reserva3.confirmar
    )

    ejecutar_prueba(
        10, "Duracion negativa",
        lambda: sala.calcular_costo(-2)
    )

    ejecutar_prueba(
        11, "Cliente con correo invalido",
        lambda: Cliente(
            "Carlos Perez", "987654", "correo_invalido"
        )
    )

    ejecutar_prueba(
        12, "Confirmar reserva duplicada",
        reserva1.confirmar
    )

    # Pruebas de impuestos y descuentos
    ejecutar_prueba(
        13, "Costo normal de sala",
        lambda: sala.calcular_costo_total(2)
    )

    ejecutar_prueba(
        14, "Costo con impuesto del 19%",
        lambda: sala.calcular_costo_total(
            2, impuesto=19
        )
    )

    ejecutar_prueba(
        15, "Costo con descuento del 10%",
        lambda: sala.calcular_costo_total(
            2, descuento=10
        )
    )

    ejecutar_prueba(
        16, "Costo con impuesto y descuento",
        lambda: sala.calcular_costo_total(
            2, impuesto=19, descuento=10
        )
    )

    # Gestion de listas internas
    gestion = GestionSistema()

    ejecutar_prueba(
        17, "Agregar cliente a lista",
        lambda: gestion.agregar_cliente(cliente)
    )

    ejecutar_prueba(
        18, "Agregar servicio a lista",
        lambda: gestion.agregar_servicio(sala)
    )

    ejecutar_prueba(
        19, "Agregar reserva a lista",
        lambda: gestion.agregar_reserva(reserva1)
    )

    ejecutar_prueba(
        20, "Consultar totales del sistema",
        gestion.obtener_totales
    )

    ejecutar_prueba(
        21, "Listar clientes",
        gestion.listar_clientes
    )

    ejecutar_prueba(
        22, "Listar servicios",
        gestion.listar_servicios
    )

    ejecutar_prueba(
        23, "Listar reservas",
        gestion.listar_reservas
    )

    # Pruebas adicionales de errores
    ejecutar_prueba(
        24, "Impuesto invalido",
        lambda: sala.calcular_costo_total(
            2, impuesto=150
        )
    )

    ejecutar_prueba(
        25, "Servicio no disponible",
        lambda: probar_servicio_no_disponible(equipo)
    )

    ejecutar_prueba(
        26, "Cancelar reserva",
        reserva3.cancelar
    )

    registrar_evento("Fin del sistema Software FJ.")
    print("\nTodas las pruebas fueron ejecutadas.")


def probar_servicio_no_disponible(servicio):
    servicio.cambiar_disponibilidad(False)
    try:
        return servicio.calcular_costo(2)
    finally:
        servicio.cambiar_disponibilidad(True)


if __name__ == "__main__":
    main()
