# Documentación de constantes – Misión Órbita

## 1. Constantes generales

| Nombre | Tipo de dato | Valor | Clasificación | Descripción |
|---|---|---:|---|---|
| `CONSUMO_COMBUSTIBLE_DIA` | int | 8 | Constante | Combustible consumido por día de viaje. |
| `CONSUMO_OXIGENO_DIA` | int | 2 | Constante | Oxígeno consumido por día por cada tripulante. |
| `CONSUMO_ENERGIA_DIA` | int | 5 | Constante | Energía consumida por día de viaje. |
| `CONSUMO_PROVISIONES_DIA` | int | 1 | Constante | Provisiones consumidas por día por cada tripulante. |
| `CANTIDAD_TRAYECTOS` | int | 2 | Constante | Cantidad de trayectos considerados: ida y regreso. |
| `RESERVA_COMBUSTIBLE` | int | 10 | Constante | Reserva adicional de combustible. |
| `OXIGENO_EMERGENCIA` | int | 5 | Constante | Reserva adicional de oxígeno para emergencias. |
| `ENERGIA_ADICIONAL` | int | 10 | Constante | Energía adicional considerada para la misión. |
| `PROVISIONES_ADICIONALES` | int | 3 | Constante | Provisiones adicionales consideradas para la misión. |
| `MARGEN_MINIMO_COMBUSTIBLE` | int | 10 | Constante | Margen mínimo de combustible requerido. |

## 2. Constantes de datos

| Nombre | Tipo de dato | Clasificación | Descripción |
|---|---|---|---|
| `DESTINOS` | tuple | Constante | Contiene los destinos disponibles y sus respectivos días de viaje. |
| `ACTIVIDADES` | tuple | Constante | Contiene las actividades disponibles, sus consumos de recursos y los puntos obtenidos. |
| `RECURSOS` | tuple | Constante | Contiene los nombres de los recursos utilizados en la misión. |
| `RECURSOS_VITALES` | tuple | Constante | Identifica los recursos vitales para la tripulación. |
| `RESULTADOS` | tuple | Constante | Contiene los posibles resultados de una misión. |

### Estructura de los datos

**DESTINOS**

Cada destino contiene:

- Posición 0: nombre del destino (`str`).
- Posición 1: días de viaje (`int`).

**ACTIVIDADES**

Cada actividad contiene:

- Posición 0: nombre de la actividad (`str`).
- Posición 1: combustible consumido (`int`).
- Posición 2: energía consumida (`int`).
- Posición 3: provisiones consumidas (`int`).
- Posición 4: puntos obtenidos (`int`).

**RECURSOS**

Contiene los recursos en el siguiente orden:

1. Combustible.
2. Oxígeno.
3. Energía.
4. Provisiones.

**RECURSOS_VITALES**

Contiene los recursos vitales en el siguiente orden:

1. Oxígeno.
2. Energía.
3. Provisiones.

**RESULTADOS**

Contiene los posibles resultados de una misión:

1. Regreso exitoso.
2. Regreso interrumpido.
3. Tripulación varada.
4. No autorizada.
5. No planificada.

## 3. Constantes de posición

| Nombre | Tipo de dato | Valor | Clasificación | Descripción |
|---|---|---:|---|---|
| `DES_NOMBRE` | int | 0 | Constante | Posición del nombre del destino. |
| `DES_DIAS` | int | 1 | Constante | Posición de los días de viaje del destino. |
| `ACT_NOMBRE` | int | 0 | Constante | Posición del nombre de la actividad. |
| `ACT_COMBUSTIBLE` | int | 1 | Constante | Posición del consumo de combustible de la actividad. |
| `ACT_ENERGIA` | int | 2 | Constante | Posición del consumo de energía de la actividad. |
| `ACT_PROVISIONES` | int | 3 | Constante | Posición del consumo de provisiones de la actividad. |
| `ACT_PUNTOS` | int | 4 | Constante | Posición de los puntos obtenidos por actividad. |
| `COMBUSTIBLE` | int | 0 | Constante | Posición del recurso combustible. |
| `OXIGENO` | int | 1 | Constante | Posición del recurso oxígeno. |
| `ENERGIA` | int | 2 | Constante | Posición del recurso energía. |
| `PROVISIONES` | int | 3 | Constante | Posición del recurso provisiones. |
| `BIT_NUMERO` | int | 0 | Constante | Posición del número de registro en la bitácora. |
| `BIT_ACTIVIDAD` | int | 1 | Constante | Posición del nombre de la actividad en la bitácora. |
| `BIT_PUNTOS` | int | 2 | Constante | Posición de los puntos obtenidos en la bitácora. |
| `MIS_NUMERO` | int | 0 | Constante | Posición del número de misión en el historial. |
| `MIS_NOMBRE` | int | 1 | Constante | Posición del nombre de la misión. |
| `MIS_DESTINO` | int | 2 | Constante | Posición del destino de la misión. |
| `MIS_RESULTADO` | int | 3 | Constante | Posición del resultado de la misión. |
| `MIS_PUNTOS` | int | 4 | Constante | Posición de los puntos obtenidos en la misión. |

---

**Proyecto:** Misión Órbita  
**Curso:** SOFT-01 Principios de Programación 1  
**Sección:** SCV3  
**Integrante:** Dylan Jesús Garos Quesada