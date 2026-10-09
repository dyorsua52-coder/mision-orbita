# ============================================================

# Archivo: ejercicio1_recursos.py

# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3

# Integrantes: [Escribir nombre completo]

# Fecha: 09/10/2026

# Versión: 1.0

# Descripción: Calcula los recursos necesarios para una misión.

# ============================================================

# Declaración de constantes para los cálculos de recursos.

COMBUSTIBLE_POR_DIA = 8
OXIGENO_POR_TRIPULANTE_DIA = 2
OXIGENO_EMERGENCIA = 5
ENERGIA_POR_DIA = 5
ENERGIA_EXPLORACION = 10
PROVISIONES_POR_TRIPULANTE_DIA = 1
PROVISIONES_EMERGENCIA = 3
RESERVA_COMBUSTIBLE = 10
DIAS_POR_VIAJE = 2

# Entrada de datos: se solicitan los datos básicos de la misión.

nombre_mision = input("Ingrese el nombre de la misión: ")
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese los días estimados para llegar al destino: "))

# Procesamiento: se calculan los recursos para el viaje de ida y regreso.

combustible_ida = dias_viaje * COMBUSTIBLE_POR_DIA
combustible_regreso = dias_viaje * COMBUSTIBLE_POR_DIA
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

oxigeno_requerido = (
dias_viaje * OXIGENO_POR_TRIPULANTE_DIA * tripulantes + OXIGENO_EMERGENCIA
)

energia_requerida = (
dias_viaje * ENERGIA_POR_DIA * DIAS_POR_VIAJE + ENERGIA_EXPLORACION
)

provisiones_requeridas = (
dias_viaje * tripulantes * DIAS_POR_VIAJE + PROVISIONES_EMERGENCIA
)

# Salida: se presenta el resumen ordenado de los recursos necesarios.

print("\n========== RESUMEN DE LA MISIÓN ==========")
print(f"Misión: {nombre_mision}")
print(f"Tripulantes: {tripulantes}")
print(f"Duración estimada hasta el destino: {dias_viaje} días")
print(f"Combustible para llegar: {combustible_ida} unidades")
print(f"Combustible para regresar: {combustible_regreso} unidades")
print(f"Reserva de combustible: {RESERVA_COMBUSTIBLE} unidades")
print(f"Combustible total requerido: {combustible_total} unidades")
print(f"Oxígeno requerido: {oxigeno_requerido} unidades")
print(f"Energía requerida: {energia_requerida} unidades")
print(f"Provisiones requeridas: {provisiones_requeridas} unidades")