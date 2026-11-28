
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


# ============================================================
# COMPONENTE A: PREPARACIÓN Y AUTORIZACIÓN
# ============================================================


# ------------------------------------------------------------
# Funcion: mostrar_destinos
# Descripcion: Muestra los destinos disponibles.
# ------------------------------------------------------------

def mostrar_destinos():
    print("Destinos disponibles:")

    numero_destino = 1

    for destino in DESTINOS:
        nombre = destino[DES_NOMBRE]
        dias = destino[DES_DIAS]

        print(numero_destino, ".", nombre, "(", dias, "días)")
        numero_destino = numero_destino + 1


# ------------------------------------------------------------
# Funcion: leer_recursos
# Descripcion: Solicita los recursos disponibles.
# ------------------------------------------------------------

def leer_recursos():
    disponibles = []

    for recurso in RECURSOS:
        cantidad = int(input("Cantidad disponible de " + recurso + ": "))
        disponibles.append(cantidad)

    return disponibles


# ------------------------------------------------------------
# Funcion: calcular_requeridos
# Descripcion: Calcula los recursos necesarios para la mision.
# ------------------------------------------------------------

def calcular_requeridos(dias_viaje, tripulantes):
    combustible = (dias_viaje * CONSUMO_COMBUSTIBLE_DIA
                   * CANTIDAD_TRAYECTOS + RESERVA_COMBUSTIBLE)

    oxigeno = (dias_viaje * CONSUMO_OXIGENO_DIA
               * CANTIDAD_TRAYECTOS * tripulantes
               + OXIGENO_EMERGENCIA)

    energia = (dias_viaje * CONSUMO_ENERGIA_DIA
               * CANTIDAD_TRAYECTOS + ENERGIA_ADICIONAL)

    provisiones = (dias_viaje * CONSUMO_PROVISIONES_DIA
                   * tripulantes * CANTIDAD_TRAYECTOS
                   + PROVISIONES_ADICIONALES)

    requeridos = [combustible, oxigeno, energia, provisiones]

    return requeridos


# ------------------------------------------------------------
# Funcion: mostrar_resumen
# Descripcion: Muestra los datos y recursos de la mision.
# ------------------------------------------------------------

def mostrar_resumen(nombre_mision, nombre_destino, dias_viaje,
                    tripulantes, disponibles, requeridos):

    print()
    print("Misión:", nombre_mision)
    print("Destino:", nombre_destino)
    print("Duración del viaje de ida:", dias_viaje, "días")
    print("Tripulantes:", tripulantes)

    for posicion in range(len(RECURSOS)):
        nombre_recurso = RECURSOS[posicion].capitalize()
        disponible = disponibles[posicion]
        requerido = requeridos[posicion]

        print(nombre_recurso + ": disponible", disponible,
              "| requerido", requerido)

    margen = disponibles[COMBUSTIBLE] - requeridos[COMBUSTIBLE]

    print("Margen adicional de combustible:", margen, "unidades")

    if margen < MARGEN_MINIMO_COMBUSTIBLE:
        print("Advertencia: el margen adicional de combustible es bajo.")


# ------------------------------------------------------------
# Funcion: autorizar_lanzamiento
# Descripcion: Comprueba si hay recursos suficientes.
# ------------------------------------------------------------

def autorizar_lanzamiento(disponibles, requeridos):
    autorizado = True

    for posicion in range(len(RECURSOS)):
        if disponibles[posicion] < requeridos[posicion]:
            autorizado = False

    return autorizado


# ============================================================
# COMPONENTE B: VIAJE DE IDA
# ============================================================


# ------------------------------------------------------------
# Funcion: calcular_consumo_diario
# Descripcion: Calcula el consumo de recursos por dia.
# ------------------------------------------------------------

def calcular_consumo_diario(tripulantes):
    combustible = CONSUMO_COMBUSTIBLE_DIA
    oxigeno = CONSUMO_OXIGENO_DIA * tripulantes
    energia = CONSUMO_ENERGIA_DIA
    provisiones = CONSUMO_PROVISIONES_DIA * tripulantes

    consumo = [combustible, oxigeno, energia, provisiones]

    return consumo


# ------------------------------------------------------------
# Funcion: viajar_al_destino
# Descripcion: Descuenta los recursos del viaje de ida.
# ------------------------------------------------------------

def viajar_al_destino(recursos, dias_viaje, tripulantes):
    consumo = calcular_consumo_diario(tripulantes)

    for posicion in range(len(RECURSOS)):
        recursos[posicion] = (
            recursos[posicion] - consumo[posicion] * dias_viaje
        )

    return recursos


# ------------------------------------------------------------
# Funcion: recursos_alcanzan
# Descripcion: Verifica si hay recursos para un dia.
# ------------------------------------------------------------

def recursos_alcanzan(recursos, consumo):
    alcanzan = True

    for posicion in range(len(RECURSOS)):
        if recursos[posicion] < consumo[posicion]:
            alcanzan = False

    return alcanzan


# ------------------------------------------------------------
# Funcion: simular_trayecto
# Descripcion: Simula un trayecto dia por dia.
# ------------------------------------------------------------

def simular_trayecto(recursos, dias, tripulantes):
    consumo = calcular_consumo_diario(tripulantes)
    dias_completados = 0
    puede_continuar = True

    while dias_completados < dias and puede_continuar:
        if recursos_alcanzan(recursos, consumo):
            for posicion in range(len(RECURSOS)):
                recursos[posicion] = (
                    recursos[posicion] - consumo[posicion]
                )

            dias_completados = dias_completados + 1

            print(
                "Día", dias_completados,
                "| Combustible:", recursos[COMBUSTIBLE],
                "| Oxígeno:", recursos[OXIGENO],
                "| Energía:", recursos[ENERGIA],
                "| Provisiones:", recursos[PROVISIONES]
            )
        else:
            puede_continuar = False

    return dias_completados

# ------------------------------------------------------------
# Funcion: mostrar_recursos
# Descripcion: Muestra los recursos disponibles.
# ------------------------------------------------------------

def mostrar_recursos(recursos):
    print("Recursos restantes:")

    for posicion in range(len(RECURSOS)):
        nombre_recurso = RECURSOS[posicion].capitalize()
        cantidad = recursos[posicion]

        print("- " + nombre_recurso + ":", cantidad, "unidades")