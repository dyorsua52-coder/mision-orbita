
# --------------------------------------------------
# Ejercicio 8: Regreso y supervivencia de la tripulación
# Misión Órbita
# --------------------------------------------------

# Constantes del programa
CONSUMO_COMBUSTIBLE = 8
CONSUMO_OXIGENO_PERSONA = 2
CONSUMO_ENERGIA = 5
CONSUMO_PROVISIONES_PERSONA = 1


# Entrada de datos
print("========================================")
print("   REGRESO Y SUPERVIVENCIA - MISIÓN ÓRBITA")
print("========================================")

tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_ida = int(input("Ingrese los días del viaje de ida: "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))


# Cálculos iniciales
combustible_necesario = dias_ida * CONSUMO_COMBUSTIBLE
consumo_oxigeno = tripulantes * CONSUMO_OXIGENO_PERSONA
consumo_provisiones = tripulantes * CONSUMO_PROVISIONES_PERSONA


# Inicialización de variables
dias_completados = 0
dia_actual = 1
regreso_activo = True


# Verificación de combustible
if combustible >= combustible_necesario:

    print("\n========== INICIO DEL REGRESO ==========")

    # Simulación del regreso día por día
    while dia_actual <= dias_ida and regreso_activo:

        print("\nDía", dia_actual)

        if (combustible >= CONSUMO_COMBUSTIBLE and
                oxigeno >= consumo_oxigeno and
                energia >= CONSUMO_ENERGIA and
                provisiones >= consumo_provisiones):

            combustible = combustible - CONSUMO_COMBUSTIBLE
            oxigeno = oxigeno - consumo_oxigeno
            energia = energia - CONSUMO_ENERGIA
            provisiones = provisiones - consumo_provisiones

            dias_completados = dias_completados + 1

            print("Día", dia_actual,
                  "| Combustible:", combustible,
                  "| Oxígeno:", oxigeno,
                  "| Energía:", energia,
                  "| Provisiones:", provisiones)

            dia_actual = dia_actual + 1

        else:

            print("Recursos insuficientes para completar el día", dia_actual)

            if combustible < CONSUMO_COMBUSTIBLE:
                print("Combustible insuficiente.")

            if oxigeno < consumo_oxigeno:
                print("Oxígeno insuficiente.")

            if energia < CONSUMO_ENERGIA:
                print("Energía insuficiente.")

            if provisiones < consumo_provisiones:
                print("Provisiones insuficientes.")

            regreso_activo = False

    # Resultado del regreso
    if dias_completados == dias_ida:

        print("\nLa tripulación regresó exitosamente a la Tierra.")

    else:

        print("\nLa tripulación no completó el regreso.")

    # Resumen de recursos
    print("\n========== RESUMEN DEL REGRESO ==========")
    print("Días completados:", dias_completados)
    print("Combustible restante:", combustible)
    print("Oxígeno restante:", oxigeno)
    print("Energía restante:", energia)
    print("Provisiones restantes:", provisiones)


else:

    # Caso B: combustible insuficiente
    print("\nLa tripulación quedó varada en el destino.")

    # Cálculo de días de supervivencia por recurso
    dias_oxigeno = oxigeno // consumo_oxigeno
    dias_energia = energia // CONSUMO_ENERGIA
    dias_provisiones = provisiones // tripulantes

    # Determinar el recurso que limita la supervivencia
    supervivencia_estimada = dias_oxigeno

    if dias_energia < supervivencia_estimada:
        supervivencia_estimada = dias_energia

    if dias_provisiones < supervivencia_estimada:
        supervivencia_estimada = dias_provisiones

    # Mostrar estimación de supervivencia
    print("\n========== SUPERVIVENCIA ==========")
    print("Días estimados de supervivencia:", supervivencia_estimada)

    print("\nRecursos que limitan la supervivencia:")

    if dias_oxigeno == supervivencia_estimada:
        print("Oxígeno.")

    if dias_energia == supervivencia_estimada:
        print("Energía.")

    if dias_provisiones == supervivencia_estimada:
        print("Provisiones.")

    print("\n========== RECURSOS DISPONIBLES ==========")
    print("Combustible:", combustible)
    print("Oxígeno:", oxigeno)
    print("Energía:", energia)
    print("Provisiones:", provisiones)


# Fin del programa