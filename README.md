# Sistema de Evaluación de Notas 

Este es un proyecto desarrollado en Python que evalúa las calificaciones de los estudiantes. Calcula el promedio exacto de tres notas y determina si el estudiante "gana" (≥ 3.0) o "reprueba" (< 3.0). Además, implementa buenas prácticas de Aseguramiento de Calidad (QA) con pruebas unitarias automatizadas usando `unittest`.

## Estructura del Proyecto


Calidad/
├── src/
│   └── evaluador.py        # Lógica de negocio, validaciones y reglas
├── tests/
│   └── test_evaluador.py   # Pruebas unitarias con runner personalizado
├── main.py                 # Punto de entrada para probar la aplicación manualmente
└── README.md               # Documentación del proyecto

## Reglas de Negocio

Rango de notas: Todas las notas deben estar entre 0.0 y 5.0. El sistema rechaza valores fuera de este límite.

Aprobación: Se requiere un promedio mayor o igual a 3.0 para retornar el estado "gana".

Reprobación: Un promedio menor a 3.0 retorna el estado "reprueba".

Precisión: Soporta el ingreso de notas con números decimales (ej. 4.1).

## Cómo ejecutar la aplicación

Asegúrate de tener Python instalado (versión 3.8 o superior). Abre una terminal, navega a la carpeta principal del proyecto (Calidad/) y ejecuta el siguiente comando para ver la evaluación manual de dos estudiantes de ejemplo:
python main.py

## Cómo ejecutar las pruebas unitarias (QA)

El proyecto cuenta con un conjunto de pruebas diseñadas para validar casos de éxito, casos límite y manejo de errores. Hemos implementado un runner personalizado que detalla las pruebas ejecutadas de forma limpia en la terminal.

Para correr la batería de pruebas, ejecuta:
python tests/test_evaluador.py

## Casos de prueba automatizados (CP):

CP-NOT-001: Evaluación de estudiante con promedio aprobatorio y notas con decimales.
CP-NOT-002: Evaluación de estudiante con promedio reprobatorio.
CP-NOT-003: Evaluación de límite exacto de aprobación (Promedio 3.0).
CP-NOT-004: Validación de error ante nota fuera del rango permitido (> 5.0).

Creado con fines educativos por: Juan David García de la Hoz, septiembre 2026