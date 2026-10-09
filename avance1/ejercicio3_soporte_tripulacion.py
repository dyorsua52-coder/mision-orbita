
# ============================================================
# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: [Escribir nombre completo]
# Fecha: 09/10/2026
# Versión: 1.0
# Descripción: Verifica si hay suficiente oxígeno y provisiones
#              para atender las necesidades de la tripulación.
# ============================================================

# Entrada de datos: solicitar recursos disponibles y requeridos.
oxigeno_disponible = int(
    input("Ingrese el oxígeno disponible: ")
)
oxigeno_requerido = int(
    input("Ingrese el oxígeno requerido: ")
)
provisiones_disponibles = int(
    input("Ingrese las provisiones disponibles: ")
)
provisiones_requeridas = int(
    input("Ingrese las provisiones requeridas: ")
)

# Decisión: comprobar si ambos recursos son suficientes.
if (
    oxigeno_disponible >= oxigeno_requerido
    and provisiones_disponibles >= provisiones_requeridas
):
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")