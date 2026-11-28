
# ============================================================
# Archivo: pruebas_componente_a.py
# Proyecto: Misión Órbita
# Componente: A - Preparación y autorización
# ============================================================

from mision_orbita import (
    mostrar_destinos,
    leer_recursos,
    calcular_requeridos,
    mostrar_resumen,
    autorizar_lanzamiento
)


# ============================================================
# PRUEBA 1: MOSTRAR DESTINOS
# ============================================================

print("===================================")
print("PRUEBA 1: MOSTRAR DESTINOS")
print("===================================")

mostrar_destinos()


# ============================================================
# PRUEBA 2: LEER RECURSOS
# ============================================================

print()
print("===================================")
print("PRUEBA 2: LEER RECURSOS")
print("===================================")

disponibles = leer_recursos()

print("Recursos ingresados:", disponibles)


# ============================================================
# PRUEBA 3: CALCULAR RECURSOS REQUERIDOS
# ============================================================

print()
print("===================================")
print("PRUEBA 3: CALCULAR RECURSOS")
print("===================================")

dias_viaje = 3
tripulantes = 2

requeridos = calcular_requeridos(dias_viaje, tripulantes)

print("Días de viaje:", dias_viaje)
print("Tripulantes:", tripulantes)
print("Recursos requeridos:", requeridos)


# ============================================================
# PRUEBA 4: MOSTRAR RESUMEN
# ============================================================

print()
print("===================================")
print("PRUEBA 4: MOSTRAR RESUMEN")
print("===================================")

mostrar_resumen(
    "Misión Luna",
    "Luna",
    dias_viaje,
    tripulantes,
    disponibles,
    requeridos
)


# ============================================================
# PRUEBA 5: AUTORIZACIÓN CON RECURSOS EXACTOS
# ============================================================

print()
print("===================================")
print("PRUEBA 5: RECURSOS EXACTOS")
print("===================================")

resultado = autorizar_lanzamiento(requeridos, requeridos)

print("Resultado esperado: True")
print("Resultado obtenido:", resultado)


# ============================================================
# PRUEBA 6: UN SOLO RECURSO INSUFICIENTE
# ============================================================

print()
print("===================================")
print("PRUEBA 6: OXÍGENO INSUFICIENTE")
print("===================================")

recursos_insuficientes = [58, 28, 40, 15]

resultado = autorizar_lanzamiento(
    recursos_insuficientes,
    requeridos
)

print("Resultado esperado: False")
print("Resultado obtenido:", resultado)


# ============================================================
# PRUEBA 7: MARGEN DE COMBUSTIBLE BAJO
# ============================================================

print()
print("===================================")
print("PRUEBA 7: MARGEN BAJO")
print("===================================")

recursos_margen_bajo = [63, 29, 40, 15]

mostrar_resumen(
    "Misión Luna",
    "Luna",
    dias_viaje,
    tripulantes,
    recursos_margen_bajo,
    requeridos
)


# ============================================================
# PRUEBA 8: MARGEN DE COMBUSTIBLE SUFICIENTE
# ============================================================

print()
print("===================================")
print("PRUEBA 8: MARGEN SUFICIENTE")
print("===================================")

recursos_margen_suficiente = [100, 30, 50, 20]

mostrar_resumen(
    "Misión Luna",
    "Luna",
    dias_viaje,
    tripulantes,
    recursos_margen_suficiente,
    requeridos
)


# ============================================================
# FIN DE LAS PRUEBAS DEL COMPONENTE A
# ============================================================
