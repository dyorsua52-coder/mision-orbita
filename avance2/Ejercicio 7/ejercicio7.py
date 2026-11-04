
# --------------------------------------------------
# Ejercicio 7: Actividades de exploración científica
# Misión Órbita
# --------------------------------------------------

# Constantes del programa
COSTO_ANALIZAR_ENERGIA = 8
COSTO_RECOLECTAR_ENERGIA = 12
COSTO_RECOLECTAR_PROVISIONES = 2
COSTO_OBSERVAR_ENERGIA = 5

PUNTOS_ANALIZAR = 10
PUNTOS_RECOLECTAR = 20
PUNTOS_OBSERVAR = 8


# Entrada de datos
print("========================================")
print("   EXPLORACIÓN CIENTÍFICA - MISIÓN ÓRBITA")
print("========================================")

energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))


# Inicialización de variables
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
exploracion_activa = True


# Ciclo principal de exploración
while exploracion_activa:

    print("\n========== MENÚ DE ACTIVIDADES ==========")
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")

    opcion = int(input("Seleccione una actividad: "))

    # Selección de actividad
    if opcion == 1:
        nombre_actividad = "Analizar terreno"
        costo_energia = COSTO_ANALIZAR_ENERGIA
        costo_provisiones = 0
        puntos_actividad = PUNTOS_ANALIZAR

    elif opcion == 2:
        nombre_actividad = "Recolectar muestra"
        costo_energia = COSTO_RECOLECTAR_ENERGIA
        costo_provisiones = COSTO_RECOLECTAR_PROVISIONES
        puntos_actividad = PUNTOS_RECOLECTAR

    elif opcion == 3:
        nombre_actividad = "Realizar observación"
        costo_energia = COSTO_OBSERVAR_ENERGIA
        costo_provisiones = 0
        puntos_actividad = PUNTOS_OBSERVAR

    elif opcion == 4:
        print("Exploración finalizada por la tripulación.")
        exploracion_activa = False

    else:
        print("Opción no válida.")

    # Verificación de recursos para las actividades
    if exploracion_activa and (opcion == 1 or opcion == 2 or opcion == 3):

        if energia >= costo_energia and provisiones >= costo_provisiones:

            # Descontar recursos
            energia = energia - costo_energia
            provisiones = provisiones - costo_provisiones

            # Actualizar contadores
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + puntos_actividad

            if opcion == 2:
                muestras_recolectadas = muestras_recolectadas + 1

            # Mostrar resultado de la actividad
            print(
                f"Actividad realizada: {nombre_actividad}. "
                f"Puntos obtenidos: {puntos_actividad}"
            )

        else:
            print(
                "Recursos insuficientes para realizar la actividad. "
                "La exploración finaliza."
            )
            exploracion_activa = False


# Resumen final
energia_restante = energia
provisiones_restantes = provisiones

print("\n========== RESUMEN FINAL ==========")
print(f"Actividades realizadas: {actividades_realizadas}")
print(f"Muestras recolectadas: {muestras_recolectadas}")
print(f"Puntos científicos: {puntos_cientificos}")
print(f"Energía restante: {energia_restante} unidades")
print(f"Provisiones restantes: {provisiones_restantes} unidades")