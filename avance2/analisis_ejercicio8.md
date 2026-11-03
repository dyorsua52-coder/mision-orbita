# Análisis del ejercicio 8: Regreso y supervivencia de la tripulación

## 1. Objetivo del programa

Simular el regreso de la tripulación a la Tierra después de completar el viaje de ida, verificando si cuenta con suficiente combustible para regresar y controlando el consumo de oxígeno, energía y provisiones durante el trayecto.

Si no existe suficiente combustible para regresar, el programa debe calcular cuántos días podría sobrevivir la tripulación según los recursos disponibles e identificar cuáles son los recursos limitantes.

## 2. Datos de entrada

- Cantidad de tripulantes.
- Cantidad de días del viaje de ida.
- Combustible disponible.
- Oxígeno disponible.
- Energía disponible.
- Provisiones disponibles.

## 3. Datos de salida

- Resultado del intento de regreso.
- Cantidad de días completados durante el regreso.
- Combustible, oxígeno, energía y provisiones restantes.
- Mensajes sobre los recursos insuficientes, si corresponde.
- Días de supervivencia estimados cuando la tripulación queda varada.
- Recursos que limitan la supervivencia.

## 4. Consumo diario de recursos

Durante cada día del viaje de regreso se consume la siguiente cantidad de recursos:

| Recurso | Consumo diario |
|---|---:|
| Combustible | 8 unidades |
| Oxígeno | 2 unidades por tripulante |
| Energía | 5 unidades |
| Provisiones | 1 unidad por tripulante |

El combustible necesario para regresar se calcula multiplicando los días del viaje de ida por 8.

## 5. Condiciones del programa

### Caso A: Combustible suficiente

Si el combustible disponible es igual o mayor al combustible necesario para regresar:

1. Se inicia la simulación del regreso.
2. Se utiliza un ciclo para representar cada día del viaje.
3. Antes de descontar los recursos, se verifica que existan cantidades suficientes de combustible, oxígeno, energía y provisiones.
4. Si todos los recursos son suficientes, se descuentan sus respectivos consumos.
5. Se aumenta el contador de días completados.
6. Se muestra el estado de los recursos al finalizar cada día.
7. Si se completan todos los días, se muestra el mensaje de regreso exitoso y los recursos restantes.
8. Si algún recurso es insuficiente, el regreso se interrumpe sin descontar los recursos de ese día.

Cuando el regreso se interrumpe, se debe indicar el día en que ocurrió y mostrar cada recurso insuficiente en el siguiente orden: oxígeno, energía y provisiones. Finalmente, se muestra el mensaje de que la tripulación no completó el regreso.

### Caso B: Combustible insuficiente

Si el combustible disponible es menor al necesario para regresar:

1. Se muestra el mensaje de que la tripulación quedó varada en el destino.
2. Se calcula cuántos días podría sobrevivir según cada recurso:
   - Días por oxígeno = oxígeno disponible dividido entre el consumo diario de oxígeno.
   - Días por energía = energía disponible dividida entre 5.
   - Días por provisiones = provisiones disponibles divididas entre la cantidad de tripulantes.
3. Se identifica el menor resultado mediante estructuras condicionales.
4. Se muestra la supervivencia estimada.
5. Se indican todos los recursos limitantes, respetando el orden: oxígeno, energía y provisiones.

Si dos o más recursos tienen el mismo valor mínimo, se deben mostrar todos los recursos que limitan la supervivencia.

## 6. Restricciones de programación

- No utilizar funciones propias.
- No utilizar listas, tuplas ni diccionarios.
- No utilizar break, continue, min ni max.
- No utilizar bibliotecas o importaciones.
- Utilizar únicamente entrada y salida por consola.
- Utilizar nombres descriptivos para las variables.
- Utilizar constantes en mayúsculas para los valores fijos.
- Utilizar estructuras condicionales y ciclos permitidos por la consigna.
- No utilizar estructuras de datos adicionales.

## 7. Tabla de variables

| Nombre | Tipo de dato | Clasificación | Descripción |
|---|---|---|---|
| tripulantes | Entero | Entrada | Cantidad de personas que forman parte de la tripulación. |
| dias_ida | Entero | Entrada | Cantidad de días utilizados en el viaje de ida. |
| combustible | Entero | Entrada | Combustible disponible para el regreso. |
| oxigeno | Entero | Entrada | Oxígeno disponible para la tripulación. |
| energia | Entero | Entrada | Energía disponible para el regreso. |
| provisiones | Entero | Entrada | Provisiones disponibles para la tripulación. |
| combustible_necesario | Entero | Intermedia | Cantidad de combustible necesaria para completar el regreso. |
| dias_completados | Entero | Intermedia | Cantidad de días completados durante el regreso. |
| dia_actual | Entero | Intermedia | Día que se está simulando durante el regreso. |
| consumo_oxigeno | Entero | Intermedia | Cantidad de oxígeno consumida diariamente por la tripulación. |
| consumo_provisiones | Entero | Intermedia | Cantidad de provisiones consumidas diariamente por la tripulación. |
| dias_oxigeno | Entero | Intermedia | Días de supervivencia estimados según el oxígeno disponible. |
| dias_energia | Entero | Intermedia | Días de supervivencia estimados según la energía disponible. |
| dias_provisiones | Entero | Intermedia | Días de supervivencia estimados según las provisiones disponibles. |
| supervivencia_estimada | Entero | Salida | Cantidad mínima de días que podría sobrevivir la tripulación. |

## 8. Valores y constantes del programa

| Nombre | Valor | Descripción |
|---|---:|---|
| CONSUMO_COMBUSTIBLE | 8 | Combustible consumido por día. |
| CONSUMO_OXIGENO_PERSONA | 2 | Oxígeno consumido diariamente por cada tripulante. |
| CONSUMO_ENERGIA | 5 | Energía consumida por día. |
| CONSUMO_PROVISIONES_PERSONA | 1 | Provisiones consumidas diariamente por cada tripulante. |

## 9. Cálculos principales

### Combustible necesario

Combustible necesario = días de ida × consumo diario de combustible.

### Consumo diario de oxígeno

Consumo de oxígeno = cantidad de tripulantes × consumo de oxígeno por persona.

### Consumo diario de provisiones

Consumo de provisiones = cantidad de tripulantes × consumo de provisiones por persona.

### Días de supervivencia

- Días por oxígeno = oxígeno disponible // consumo diario de oxígeno.
- Días por energía = energía disponible // consumo diario de energía.
- Días por provisiones = provisiones disponibles // consumo diario de provisiones.

La supervivencia estimada corresponde al menor de los tres resultados. La identificación del resultado se realiza mediante condiciones, sin utilizar la función `min()`.

## 10. Resumen de la lógica del programa

1. Solicitar los datos de entrada de la tripulación y los recursos disponibles.
2. Calcular el combustible necesario para regresar.
3. Comparar el combustible disponible con el necesario.
4. Si existe suficiente combustible, iniciar la simulación del regreso.
5. Verificar diariamente que todos los recursos sean suficientes antes de descontarlos.
6. Si los recursos son suficientes, descontar el consumo y aumentar los días completados.
7. Si algún recurso es insuficiente, interrumpir el regreso sin modificar los recursos de ese día.
8. Si se completan todos los días, mostrar el regreso exitoso y los recursos restantes.
9. Si no existe suficiente combustible, calcular los días de supervivencia según cada recurso.
10. Identificar la supervivencia estimada y todos los recursos limitantes.
11. Mostrar los resultados correspondientes al caso ejecutado.