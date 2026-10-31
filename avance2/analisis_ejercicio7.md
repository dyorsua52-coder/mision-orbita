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

## 7. Restricciones de programación
- No utilizar funciones propias.
- No utilizar listas, tuplas ni diccionarios.
- No utilizar break, continue, min ni max.
- Utilizar únicamente entrada y salida por consola.
- Utilizar nombres descriptivos para las variables.