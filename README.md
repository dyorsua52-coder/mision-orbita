# Misión Órbita

## Descripción del proyecto

Misión Órbita es un proyecto desarrollado en Python para el curso SOFT-01 — Principios de Programación 1 de CENFOTEC.

El proyecto consiste en desarrollar un simulador básico de una misión de exploración espacial. Mediante diferentes programas independientes, se realizan cálculos de recursos, verificaciones de seguridad, actividades científicas y simulaciones relacionadas con la supervivencia de la tripulación.

El proyecto está organizado en dos avances, cada uno con sus respectivos programas, análisis, diagramas de flujo y casos de prueba.

## Información académica

- **Universidad:** CENFOTEC
- **Curso:** SOFT-01 — Principios de Programación 1
- **Sección:** SCV3
- **Periodo:** C3-2026
- **Docente:** Verónica Mora Lezcano

## Integrante

- Dylan Garos Quesada

## Estructura del proyecto

```text
mision-orbita/
│
├── avance1/
│
├── avance2/
│   │
│   ├── Ejercicio 7/
│   │   ├── pruebas/
│   │   ├── analisis_ejercicio7.md
│   │   ├── diagrama_ejercicio7.png
│   │   └── ejercicio7.py
│   │
│   └── Ejercicio 8/
│       ├── pruebas/
│       ├── analisis_ejercicio8.md
│       ├── diagrama_ejercicio8.png
│       └── ejercicio8.py
│
├── .gitattributes
└── README.md
```

## Avance 1

El primer avance contiene cuatro programas independientes:

1. **Ejercicio 1:** cálculo de recursos necesarios para una misión.
2. **Ejercicio 2:** verificación del combustible disponible.
3. **Ejercicio 3:** verificación de oxígeno y provisiones para la tripulación.
4. **Ejercicio 4:** autorización inicial de lanzamiento.

Los programas se encuentran dentro de la carpeta `avance1/`.

## Avance 2

El segundo avance contiene dos ejercicios:

### Ejercicio 7: Actividades de exploración científica

Simula las actividades científicas que puede realizar la tripulación al llegar al destino.

El programa permite analizar el terreno, recolectar muestras y realizar observaciones, controlando el consumo de energía y provisiones, así como los puntos científicos obtenidos.

Archivos:
- `analisis_ejercicio7.md`
- `ejercicio7.py`
- `diagrama_ejercicio7.png`
- Carpeta `pruebas/` con cuatro casos de prueba y sus evidencias.

### Ejercicio 8: Regreso y supervivencia de la tripulación

Simula el regreso de la tripulación a la Tierra, verificando la disponibilidad de combustible, oxígeno, energía y provisiones.

Cuando no existe suficiente combustible, el programa calcula los días estimados de supervivencia e identifica los recursos que limitan la supervivencia.

Archivos:
- `analisis_ejercicio8.md`
- `ejercicio8.py`
- `diagrama_ejercicio8.png`
- Carpeta `pruebas/` con cuatro casos de prueba y sus evidencias.

## Instrucciones de ejecución

1. Abrir la carpeta principal del proyecto en Visual Studio Code.
2. Abrir una terminal desde **Terminal → New Terminal**.
3. Ejecutar el programa deseado utilizando Python.

Ejemplos para el segundo avance:

```bash
python "avance2/Ejercicio 7/ejercicio7.py"
```

```bash
python "avance2/Ejercicio 8/ejercicio8.py"
```

4. Introducir los datos solicitados por la consola.

Para ejecutar los programas del primer avance, se debe utilizar la ruta correspondiente al archivo `.py` dentro de `avance1/`.

## Convenciones y restricciones

- Utilizar nombres descriptivos de variables en `snake_case`.
- Declarar las constantes con nombres en mayúsculas.
- Mantener una indentación de cuatro espacios.
- Incluir encabezados y comentarios que documenten los bloques lógicos.
- Utilizar entrada y salida por consola.
- Mantener cada ejercicio en un archivo `.py` independiente.
- Respetar las restricciones de programación establecidas para cada avance.

## Tecnologías utilizadas

- Python
- Visual Studio Code
- Git
- GitHub

## Documentación y pruebas

Cada ejercicio del segundo avance cuenta con su análisis, diagrama de flujo y documentación de casos de prueba.

Las evidencias de ejecución se encuentran en las carpetas `pruebas/` correspondientes a cada ejercicio.