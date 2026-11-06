# Análisis del ejercicio 8: Regreso y supervivencia de la tripulación

## 1. Objetivo del programa

Simular el regreso de la tripulación a la Tierra después de completar el viaje de ida, verificando si cuenta con suficiente combustible para regresar y controlando el consumo de oxígeno, energía y provisiones durante el trayecto.

Si no existe suficiente combustible para regresar, el programa debe calcular cuántos días podría sobrevivir la tripulación según los recursos disponibles e identificar cuáles limitan su supervivencia.

## 2. Datos de entrada

El programa solicita los siguientes datos:

- `tripulantes`: cantidad de personas que conforman la tripulación.
- `dias_ida`: cantidad de días que duró el viaje de ida.
- `combustible`: cantidad de combustible disponible.
- `oxigeno`: cantidad de oxígeno disponible.
- `energia`: cantidad de energía disponible.
- `provisiones`: cantidad de provisiones disponibles.

**Supuestos de entrada:**

- Se asume que todos los datos ingresados son números enteros no negativos.
- La cantidad de tripulantes debe ser mayor que cero para realizar correctamente los cálculos de consumo y supervivencia.
- El programa trabaja con datos válidos proporcionados por el usuario.

## 3. Datos de salida

El programa muestra:

- Si la tripulación logró regresar a la Tierra.
- La cantidad de días completados durante el regreso.
- Los recursos restantes después de cada día.
- Los recursos insuficientes cuando no se puede completar un día.
- Los días estimados de supervivencia cuando no hay suficiente combustible.
- Los recursos que limitan la supervivencia.

## 4. Constantes y consumo de recursos

El programa utiliza las siguientes constantes:

| Constante | Valor | Descripción |
|---|---:|---|
| `CONSUMO_COMBUSTIBLE` | 8 | Combustible consumido por día. |
| `CONSUMO_OXIGENO_PERSONA` | 2 | Oxígeno consumido por persona al día. |
| `CONSUMO_ENERGIA` | 5 | Energía consumida por día. |
| `CONSUMO_PROVISIONES_PERSONA` | 1 | Provisiones consumidas por persona al día. |

El combustible necesario para regresar se calcula multiplicando los días del viaje de ida por el consumo diario de combustible.

El consumo diario de oxígeno y provisiones depende de la cantidad de tripulantes.

## 5. Lógica del programa

### Caso A: combustible suficiente

Si el combustible disponible es mayor o igual al combustible necesario para regresar:

1. Se inicia la simulación del regreso.
2. Se utiliza un ciclo `while` para recorrer cada día del viaje.
3. Antes de completar cada día, se verifica que existan suficientes recursos:
   - Combustible.
   - Oxígeno.
   - Energía.
   - Provisiones.
4. Si todos los recursos son suficientes, se descuentan los consumos correspondientes.
5. Se aumenta el contador de días completados.
6. Se muestran los recursos restantes.
7. Si algún recurso es insuficiente, no se descuentan recursos de ese día y se informa cuál o cuáles recursos faltan.
8. Se detiene la simulación del regreso.
9. Finalmente, se indica si la tripulación logró regresar y se muestra el resumen de recursos.

### Caso B: combustible insuficiente

Si el combustible disponible es menor que el necesario para regresar:

1. Se informa que la tripulación quedó varada en el destino.
2. Se calcula cuántos días podría sobrevivir según cada recurso:
   - Días de oxígeno = oxígeno disponible dividido entre el consumo diario de oxígeno.
   - Días de energía = energía disponible dividido entre el consumo diario de energía.
   - Días de provisiones = provisiones disponibles divididas entre la cantidad de tripulantes.
3. Se utiliza división entera para obtener días completos de supervivencia.
4. Se determina el menor resultado mediante estructuras condicionales, sin utilizar `min()`.
5. Se muestra la cantidad estimada de días de supervivencia.
6. Se identifican todos los recursos que limitan la supervivencia, incluyendo los empates.
7. Se muestran los recursos disponibles.

## 6. Variables del programa

| Variable | Tipo | Descripción |
|---|---|---|
| `tripulantes` | Entero | Cantidad de personas de la tripulación. |
| `dias_ida` | Entero | Días que duró el viaje de ida. |
| `combustible` | Entero | Combustible disponible. |
| `oxigeno` | Entero | Oxígeno disponible. |
| `energia` | Entero | Energía disponible. |
| `provisiones` | Entero | Provisiones disponibles. |
| `combustible_necesario` | Entero | Combustible requerido para regresar. |
| `consumo_oxigeno` | Entero | Consumo diario de oxígeno de toda la tripulación. |
| `consumo_provisiones` | Entero | Consumo diario de provisiones de toda la tripulación. |
| `dias_completados` | Entero | Días completados durante el regreso. |
| `dia_actual` | Entero | Día que se está simulando. |
| `regreso_activo` | Booleano | Indica si la simulación del regreso continúa. |
| `dias_oxigeno` | Entero | Días de supervivencia según el oxígeno. |
| `dias_energia` | Entero | Días de supervivencia según la energía. |
| `dias_provisiones` | Entero | Días de supervivencia según las provisiones. |
| `supervivencia_estimada` | Entero | Menor cantidad de días de supervivencia calculada. |

## 7. Cálculos principales

**Combustible necesario:**

`combustible_necesario = dias_ida * CONSUMO_COMBUSTIBLE`

**Consumo diario de oxígeno:**

`consumo_oxigeno = tripulantes * CONSUMO_OXIGENO_PERSONA`

**Consumo diario de provisiones:**

`consumo_provisiones = tripulantes * CONSUMO_PROVISIONES_PERSONA`

**Días de supervivencia por oxígeno:**

`dias_oxigeno = oxigeno // consumo_oxigeno`

**Días de supervivencia por energía:**

`dias_energia = energia // CONSUMO_ENERGIA`

**Días de supervivencia por provisiones:**

`dias_provisiones = provisiones // tripulantes`

Para determinar la supervivencia estimada, se comparan los tres resultados mediante estructuras condicionales y se conserva el menor valor.

## 8. Estructuras de programación utilizadas

- Variables para almacenar los datos de entrada y los resultados.
- Constantes para representar los consumos de recursos.
- Operaciones aritméticas para calcular los consumos y la supervivencia.
- Condicionales `if` para verificar los recursos disponibles y determinar los resultados.
- Ciclo `while` para simular el regreso día por día.
- Operadores de comparación para evaluar las condiciones.
- Operador lógico `and` para comprobar que todos los recursos sean suficientes.

## 9. Restricciones de programación

El programa respeta las restricciones establecidas para el proyecto:

- No utiliza funciones propias (`def`).
- No utiliza listas, tuplas ni diccionarios.
- No utiliza bibliotecas ni importaciones.
- No utiliza `min()`, `max()`, `break`, `continue`, `exit()` ni `quit()`.
- Utiliza únicamente entrada y salida por consola.
- Utiliza nombres descriptivos para las variables.
- Las constantes se escriben en mayúsculas.
- Utiliza estructuras condicionales y ciclos permitidos.

## 10. Resultado esperado

El programa debe permitir simular dos situaciones:

- Cuando existe combustible suficiente, la tripulación intenta regresar y consume los recursos correspondientes por cada día completado.
- Cuando no existe combustible suficiente, la tripulación queda varada y el programa calcula los días estimados de supervivencia según el recurso más limitado.

En ambos casos se deben mostrar resultados claros y comprensibles para el usuario.

## 11. Resumen del funcionamiento

1. Solicitar los datos de entrada.
2. Calcular el combustible necesario para regresar.
3. Calcular el consumo diario de oxígeno y provisiones.
4. Verificar si existe combustible suficiente.
5. Si existe combustible suficiente, iniciar la simulación diaria del regreso.
6. Verificar los recursos antes de completar cada día.
7. Descontar los recursos y actualizar los días completados cuando sea posible.
8. Si no existe combustible suficiente, calcular los días de supervivencia por recurso.
9. Determinar el recurso o los recursos que limitan la supervivencia.
10. Mostrar el resultado correspondiente.
11. Finalizar el programa.