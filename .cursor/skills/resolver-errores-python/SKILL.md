---
name: resolver-errores-python
description: Diagnostica y corrige errores en scripts Python del repositorio Stack 1. Usar cuando el usuario pegue un traceback, reporte que un script falla, mencione columnas faltantes, archivos no encontrados, tipos incorrectos o pida hacer el código más robusto.
---

# Resolver errores — Stack 1

## Leer el traceback

Leer de abajo hacia arriba. Identificar:

1. Tipo de error (`FileNotFoundError`, `KeyError`, `ValueError`, etc.)
2. Archivo y línea donde falló
3. Mensaje concreto del error

## Errores frecuentes en este stack

| Error | Causa habitual | Corrección |
|-------|----------------|------------|
| `FileNotFoundError` | Ruta incorrecta en `config.py` | Verificar `RUTA_DATOS_ENTRADA` y que el archivo exista |
| `KeyError` | Columna con nombre distinto al esperado | Validar columnas al cargar; mensaje con columnas encontradas vs requeridas |
| `ValueError` (tipos) | Fechas o números en formato incorrecto | Convertir con manejo de errores; informar filas problemáticas |
| Filas vacías | Celdas sin dato | Filtrar o rellenar según regla de negocio; no fallar en silencio |

## Corrección mínima

- Corregir la causa, no reescribir todo el script.
- Agregar `try/except` solo donde corresponda (lectura de archivos, validación).
- Mensajes en español: qué falló y qué debe revisar el usuario.

## Plantilla de respuesta al usuario

1. Explicar la causa en lenguaje claro.
2. Mostrar el cambio mínimo necesario.
3. Indicar cómo reprobar: `python scripts/nombre.py`

## Robustez desde el prompt

Si el usuario pide prevención:

- Validar columnas antes de procesar.
- No fallar si hay filas vacías (omitir o informar cantidad).
- Registrar en consola filas procesadas y errores parciales.
