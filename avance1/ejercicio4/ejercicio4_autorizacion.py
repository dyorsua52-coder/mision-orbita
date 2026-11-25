
# ============================================================
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: [Escribir nombre completo]
# Fecha: 09/10/2026
# Versión: 1.0
# Descripción: Determina si una misión cumple los requisitos
#              necesarios para autorizar su lanzamiento.
# ============================================================

# Declaración de constantes para los cálculos.
RESERVA_COMBUSTIBLE = 10

# Entrada de datos: solicitar los recursos disponibles
# y los recursos requeridos para la misión.
combustible_disponible = int(
    input("Ingrese el combustible disponible: ")
)
combustible_ida = int(
    input("Ingrese el combustible requerido para la ida: ")
)
combustible_regreso = int(
    input("Ingrese el combustible requerido para el regreso: ")
)

oxigeno_disponible = int(
    input("Ingrese el oxígeno disponible: ")
)
oxigeno_requerido = int(
    input("Ingrese el oxígeno requerido: ")
)

energia_disponible = int(
    input("Ingrese la energía disponible: ")
)
energia_requerida = int(
    input("Ingrese la energía requerida: ")
)

provisiones_disponibles = int(
    input("Ingrese las provisiones disponibles: ")
)
provisiones_requeridas = int(
    input("Ingrese las provisiones requeridas: ")
)

# Procesamiento: calcular el combustible total requerido.
combustible_total_requerido = (
    combustible_ida
    + combustible_regreso
    + RESERVA_COMBUSTIBLE
)

# Decisión: comprobar si todos los recursos son suficientes.
if (
    combustible_disponible >= combustible_total_requerido
    and oxigeno_disponible >= oxigeno_requerido
    and energia_disponible >= energia_requerida
    and provisiones_disponibles >= provisiones_requeridas
):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")