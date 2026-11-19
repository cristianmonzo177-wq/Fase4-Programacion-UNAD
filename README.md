
# Sistema Integral de Gestion - Software FJ

## Universidad Nacional Abierta y a Distancia - UNAD

**Curso:** Programacion 213023  
**Actividad:** Fase 4 - Practicas simuladas  
**Lenguaje:** Python 3  
**Proyecto:** Sistema Integral de Gestion de Clientes, Servicios y Reservas

## 1. Descripcion del proyecto

Software FJ es un sistema desarrollado en Python mediante
programacion orientada a objetos (POO), cuyo objetivo es
gestionar clientes, servicios y reservas.

El programa permite registrar clientes, consultar servicios,
calcular costos, confirmar y cancelar reservas, validar
operaciones y controlar errores mediante excepciones
personalizadas.

## 2. Funcionalidades principales

- Registro y validacion de clientes.
- Gestion de salas de reuniones.
- Alquiler de equipos.
- Asesorias especializadas.
- Creacion, confirmacion y cancelacion de reservas.
- Calculo de costos de servicios.
- Aplicacion de impuestos y descuentos.
- Gestion de listas internas.
- Manejo de excepciones personalizadas.
- Encadenamiento de excepciones.
- Registro de eventos y errores en sistema.log.
- Ejecucion de 26 pruebas simuladas.

## 3. Conceptos de programacion implementados

- Abstraccion mediante clases abstractas.
- Herencia entre clases.
- Encapsulamiento de atributos.
- Polimorfismo mediante metodos redefinidos.
- Parametros opcionales en metodos.
- Manejo de excepciones con try, except, else y finally.
- Encadenamiento de excepciones con raise ... from error.
- Manejo de listas internas.
- Registro de eventos con el modulo logging.

## 4. Estructura del proyecto

- entidad.py: clase abstracta Entidad.
- cliente.py: registro y validacion de clientes.
- servicio.py: clase abstracta Servicio y calculo de costos.
- reserva_sala.py: gestion de salas de reuniones.
- alquiler_equipo.py: gestion del alquiler de equipos.
- asesoria_especializada.py: gestion de asesorias.
- reserva.py: administracion de reservas.
- gestion_sistema.py: almacenamiento y consulta de listas.
- excepciones.py: excepciones personalizadas.
- registro_logs.py: registro de eventos y errores.
- main.py: programa principal y pruebas simuladas.
- README.md: documentacion del proyecto.

## 5. Requisitos de ejecucion

- Tener instalado Python 3.
- Descargar o clonar el repositorio.
- Mantener todos los archivos .py en la misma carpeta.

El proyecto utiliza bibliotecas estandar de Python,
por lo que no requiere instalar paquetes externos.

## 6. Instrucciones de ejecucion

1. Descargar el repositorio desde GitHub.
2. Extraer el archivo ZIP.
3. Abrir la carpeta que contiene main.py.
4. Abrir CMD desde esa carpeta.
5. Ejecutar el siguiente comando:

```cmd
py main.py
```

En sistemas donde Python se ejecuta con el comando
python, tambien puede utilizarse:

```cmd
python main.py
```

## 7. Pruebas del sistema

El archivo main.py contiene 26 pruebas simuladas:

- Pruebas 1 a 9: consultas, calculos y confirmaciones.
- Pruebas 10 a 12: validacion de errores.
- Pruebas 13 a 16: impuestos y descuentos.
- Pruebas 17 a 23: gestion de listas internas.
- Prueba 24: impuesto invalido.
- Prueba 25: servicio no disponible.
- Prueba 26: cancelacion de reserva.

Las pruebas con errores intencionales permiten
comprobar el manejo de excepciones.

## 8. Registro de eventos

El sistema utiliza el modulo logging para registrar
eventos exitosos, errores y advertencias.

Los registros se almacenan en el archivo sistema.log,
que se genera durante la ejecucion del programa.

## 9. Resultados

Durante la ejecucion local se comprobaron los 26
escenarios definidos en main.py.

Los resultados permitieron verificar el funcionamiento
de las operaciones principales, los calculos de costos,
las listas internas y el manejo de errores controlados.

## 10. Conclusion

El desarrollo de Software FJ permitio aplicar los
principios de la programacion orientada a objetos
en un sistema de gestion de clientes, servicios y
reservas.

La implementacion de excepciones personalizadas,
registros de eventos y pruebas simuladas contribuye
a mejorar la organizacion y confiabilidad del codigo.

## 11. Repositorio

https://github.com/cristianmonzo177-wq/Fase4-Programacion-UNAD
