
# UNAD - Programacion 213023
# Fase 4 - Sistema Software FJ
# Registro de errores y eventos

import logging


# Configuracion del sistema de logs
logging.basicConfig(
    filename="sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


# Registrar eventos exitosos
def registrar_evento(mensaje):
    logging.info(mensaje)


# Registrar errores del sistema
def registrar_error(mensaje):
    logging.error(mensaje)


# Registrar advertencias
def registrar_advertencia(mensaje):
    logging.warning(mensaje)
