
# ============================================================
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: [Escribir nombre completo]
# Fecha: 09/10/2026
# Versión: 1.0
# Descripción: Calcula el combustible requerido y advierte
#              cuando el margen adicional es bajo.
# ============================================================

# Declaración de constantes para los cálculos.
RESERVA_COMBUSTIBLE = 10
MARGEN_MINIMO_COMBUSTIBLE = 10

# Entrada de datos: solicitar las cantidades de combustible.
combustible_disponible = int(
    input("Ingrese el combustible disponible: ")
)
combustible_ida = int(
    input("Ingrese el combustible requerido para la ida: ")
)
combustible_regreso = int(
    input("Ingrese el combustible requerido para el regreso: ")
)

# Procesamiento: calcular el combustible total y el margen.
combustible_total_requerido = (
    combustible_ida
    + combustible_regreso
    + RESERVA_COMBUSTIBLE
)

margen_adicional = (
    combustible_disponible - combustible_total_requerido
)

# Decisión: verificar si el margen adicional es bajo.
if margen_adicional < MARGEN_MINIMO_COMBUSTIBLE:
    print(
        "Advertencia: el margen adicional de combustible es bajo."
    )

# Salida: mostrar el resumen de combustible.
print("\n========== RESUMEN DE COMBUSTIBLE ==========")
print(f"Combustible disponible: {combustible_disponible} unidades")
print(f"Combustible para la ida: {combustible_ida} unidades")
print(f"Combustible para el regreso: {combustible_regreso} unidades")
print(f"Reserva de combustible: {RESERVA_COMBUSTIBLE} unidades")
print(
    f"Combustible total requerido: "
    f"{combustible_total_requerido} unidades"
)
print(f"Margen adicional: {margen_adicional} unidades")