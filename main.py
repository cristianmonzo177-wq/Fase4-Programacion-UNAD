
# UNAD - Programacion 213023
# Fase 4 - Practicas simuladas
# Sistema Integral de Gestion - Software FJ

from cliente import Cliente
from reserva_sala import ReservaSala
from alquiler_equipo import AlquilerEquipo
from asesoria_especializada import AsesoriaEspecializada
from reserva import Reserva

from excepciones import ErrorSistema
from registro_logs import registrar_evento, registrar_error


def ejecutar_prueba(numero, descripcion, operacion):
    print(f"\nPRUEBA {numero}: {descripcion}")

    try:
        resultado = operacion()

    except (ErrorSistema, ValueError, TypeError) as error:
        print(f"Error controlado: {error}")
        registrar_error(
            f"Prueba {numero}: {error}"
        )

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
        "Ana Martinez",
        "123456789",
        "ana@correo.com"
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

    # Operaciones exitosas
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

    # Pruebas de errores controlados
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

    registrar_evento("Fin del sistema Software FJ.")
    print("\nTodas las pruebas fueron ejecutadas.")


if __name__ == "__main__":
    main()
