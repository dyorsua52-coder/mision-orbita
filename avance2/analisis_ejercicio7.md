# Análisis del ejercicio 7: Actividades de exploración científica

## 1. Objetivo del programa

Simular las actividades de exploración científica que puede realizar la tripulación al llegar al destino, controlando la energía, las provisiones y los puntos científicos obtenidos.

## 2. Datos de entrada

- Energía disponible al llegar.
- Provisiones disponibles al llegar.
- Opción seleccionada en el menú.

## 3. Datos de salida

- Actividades realizadas.
- Muestras recolectadas.
- Puntos científicos acumulados.
- Energía restante.
- Provisiones restantes.
- Mensajes sobre las actividades y el estado de la exploración.

## 4. Variables iniciales

- puntos_cientificos = 0
- actividades_realizadas = 0
- muestras_recolectadas = 0

## 5. Reglas de las actividades

| Actividad | Energía | Provisiones | Puntos |
|---|---:|---:|---:|
| Analizar terreno | 8 | 0 | 10 |
| Recolectar muestra | 12 | 2 | 20 |
| Realizar observación | 5 | 0 | 8 |
| Finalizar exploración | 0 | 0 | 0 |

## 6. Condiciones del programa

- El menú debe repetirse hasta que la exploración finalice.
- Se deben verificar los recursos antes de realizar una actividad.
- Si los recursos son suficientes, se descuentan y se actualizan los contadores.
- Si los recursos son insuficientes, la exploración finaliza sin modificar los valores.
- La opción 4 finaliza la exploración.
- Una opción numérica no válida muestra un mensaje y permite repetir el menú.
- Si se selecciona una actividad y faltan recursos, se finaliza la exploración inmediatamente.
- Al finalizar se debe mostrar el resumen de las actividades, muestras, puntos y recursos restantes.

## 7. Restricciones de programación

- No utilizar funciones propias.
- No utilizar listas, tuplas ni diccionarios.
- No utilizar break, continue, min ni max.
- Utilizar únicamente entrada y salida por consola.
- Utilizar nombres descriptivos para las variables.
- Utilizar constantes en mayúsculas para los valores fijos.
- Utilizar estructuras condicionales y ciclos permitidos por la consigna.

## 8. Tabla de variables

| Nombre | Tipo de dato | Clasificación | Descripción |
|---|---|---|---|
| energia | Entero | Entrada | Energía disponible al llegar al destino. |
| provisiones | Entero | Entrada | Provisiones disponibles al llegar al destino. |
| opcion | Entero | Entrada | Opción seleccionada en el menú. |
| puntos_cientificos | Entero | Intermedia | Acumula los puntos obtenidos durante la exploración. |
| actividades_realizadas | Entero | Intermedia | Cuenta las actividades realizadas exitosamente. |
| muestras_recolectadas | Entero | Intermedia | Cuenta las muestras recolectadas. |
| nombre_actividad | Cadena | Intermedia | Nombre de la actividad seleccionada. |
| costo_energia | Entero | Intermedia | Energía necesaria para realizar la actividad. |
| costo_provisiones | Entero | Intermedia | Provisiones necesarias para realizar la actividad. |
| puntos_actividad | Entero | Intermedia | Puntos que otorga la actividad seleccionada. |
| energia_restante | Entero | Salida | Energía disponible al finalizar la exploración. |
| provisiones_restantes | Entero | Salida | Provisiones disponibles al finalizar la exploración. |

## 9. Valores iniciales

| Variable | Valor inicial |
|---|---:|
| puntos_cientificos | 0 |
| actividades_realizadas | 0 |
| muestras_recolectadas | 0 |

## 10. Constantes del programa

| Nombre | Valor | Descripción |
|---|---:|---|
| COSTO_ANALIZAR_ENERGIA | 8 | Energía necesaria para analizar el terreno. |
| COSTO_RECOLECTAR_ENERGIA | 12 | Energía necesaria para recolectar una muestra. |
| COSTO_RECOLECTAR_PROVISIONES | 2 | Provisiones necesarias para recolectar una muestra. |
| COSTO_OBSERVAR_ENERGIA | 5 | Energía necesaria para realizar una observación. |
| PUNTOS_ANALIZAR | 10 | Puntos obtenidos al analizar el terreno. |
| PUNTOS_RECOLECTAR | 20 | Puntos obtenidos al recolectar una muestra. |
| PUNTOS_OBSERVAR | 8 | Puntos obtenidos al realizar una observación. |

## 11. Resumen de la lógica del programa

1. Solicitar la energía y las provisiones disponibles.
2. Inicializar los contadores en cero.
3. Mostrar el menú de actividades.
4. Solicitar una opción a la tripulación.
5. Verificar la opción seleccionada.
6. Comprobar si existen recursos suficientes para realizar la actividad.
7. Si los recursos son suficientes, descontarlos y actualizar los contadores.
8. Si los recursos son insuficientes, finalizar la exploración sin modificar los valores.
9. Si se selecciona la opción 4, finalizar la exploración.
10. Mostrar el resumen final de la exploración.