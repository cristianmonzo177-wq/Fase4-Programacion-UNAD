
# UNAD - Programacion 213023
# Fase 4 - Sistema Software FJ
# Excepciones personalizadas


# Excepcion general del sistema
class ErrorSistema(Exception):
    """Clase base para los errores del sistema."""
    pass


# Error relacionado con los clientes
class ClienteInvalidoError(ErrorSistema):
    """Se genera cuando los datos del cliente son invalidos."""
    pass


# Error relacionado con los servicios
class ServicioNoDisponibleError(ErrorSistema):
    """Se genera cuando un servicio no esta disponible."""
    pass


# Error relacionado con las reservas
class ReservaInvalidaError(ErrorSistema):
    """Se genera cuando una reserva es incorrecta."""
    pass


# Error relacionado con los calculos
class CalculoInvalidoError(ErrorSistema):
    """Se genera cuando un calculo presenta inconsistencias."""
    pass


# Error relacionado con operaciones no permitidas
class OperacionNoPermitidaError(ErrorSistema):
    """Se genera cuando una operacion no esta permitida."""
    pass
