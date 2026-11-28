
# Casos de prueba – Componente A

Proyecto: Misión Órbita
Componente: A – Preparación y autorización

| ID | Escenario | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|
| CP-A-01 | Selección de destino no válida | Rechazar opción incorrecta | Pendiente de integración del menú | Pendiente |
| CP-A-02 | Recursos exactamente iguales a los requeridos | Autorización True | True | Exitoso |
| CP-A-03 | Un solo recurso insuficiente | Autorización False | False por oxígeno insuficiente | Exitoso |
| CP-A-04 | Margen de combustible bajo | 5 unidades y advertencia | 5 unidades y advertencia | Exitoso |
| CP-A-05 | Margen de combustible suficiente | 42 unidades sin advertencia | 42 unidades sin advertencia | Exitoso |

## Evidencias

- evidencia_ejecucion_pruebas_componente_a.png
- evidencia_componente_a_casos_02_05.png

## Observaciones

El caso CP-A-01 queda pendiente para cuando se integre el menú de selección de destino.
Los demás casos fueron ejecutados y sus resultados coinciden con los esperados.
