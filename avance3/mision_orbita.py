
# ============================================================

# Archivo: mision_orbita.py

# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3

# Integrantes: Dylan Jesús Garos Quesada

# Fecha: 25/11/2026          Versión: 1.0

# Descripción: Sistema integrado Misión Órbita.

# ============================================================


# ============================================================
# DECLARACIÓN DE CONSTANTES
# ============================================================

# Valores fijos utilizados en los cálculos

CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_DIA = 1

CANTIDAD_TRAYECTOS = 2
RESERVA_COMBUSTIBLE = 10
OXIGENO_EMERGENCIA = 5
ENERGIA_ADICIONAL = 10
PROVISIONES_ADICIONALES = 3
MARGEN_MINIMO_COMBUSTIBLE = 10

# Destinos: (nombre, días de viaje)

DESTINOS = (
    ("Luna", 3),
    ("Marte", 5),
    ("Europa", 7)
)

# Actividades: (nombre, combustible, energía, provisiones, puntos)

ACTIVIDADES = (
    ("Analizar terreno", 0, 8, 0, 10),
    ("Recolectar muestra", 0, 12, 2, 20),
    ("Realizar observación", 0, 5, 0, 8),
    ("Sobrevolar la zona", 15, 3, 0, 25)
)

RECURSOS = ("combustible", "oxígeno", "energía", "provisiones")

RECURSOS_VITALES = ("oxígeno", "energía", "provisiones")

RESULTADOS = (
    "Regreso exitoso",
    "Regreso interrumpido",
    "Tripulación varada",
    "No autorizada",
    "No planificada"
)

# ============================================================
# CONSTANTES DE POSICIÓN
# ============================================================

# Columnas de DESTINOS

DES_NOMBRE = 0
DES_DIAS = 1

# Columnas de ACTIVIDADES

ACT_NOMBRE = 0
ACT_COMBUSTIBLE = 1
ACT_ENERGIA = 2
ACT_PROVISIONES = 3
ACT_PUNTOS = 4

# Posiciones de los recursos

COMBUSTIBLE = 0
OXIGENO = 1
ENERGIA = 2
PROVISIONES = 3

# Columnas de la matriz bitacora

BIT_NUMERO = 0
BIT_ACTIVIDAD = 1
BIT_PUNTOS = 2

# Columnas de la matriz historial

MIS_NUMERO = 0
MIS_NOMBRE = 1
MIS_DESTINO = 2
MIS_RESULTADO = 3
MIS_PUNTOS = 4