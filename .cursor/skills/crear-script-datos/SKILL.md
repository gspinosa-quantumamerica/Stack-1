---
name: crear-script-datos
description: Crea scripts Python de lectura, transformación y exportación de datos con pandas y openpyxl en el repositorio Stack 1. Usar cuando el usuario pida crear, modificar o ampliar scripts en scripts/, procesar Excel o CSV, filtrar, agrupar, calcular o exportar resultados.
---

# Crear script de datos — Stack 1

## Antes de escribir código

1. Leer `config.py` para rutas y columnas esperadas.
2. Confirmar que la librería está en `requirements.txt`. No agregar dependencias nuevas sin aprobación de IT.
3. Ubicar el script en `scripts/`, un archivo por tarea.

## Estructura del script

Separar en funciones cortas:

1. **Carga** — leer desde la ruta en `config.py`
2. **Validación** — verificar que el archivo existe y tiene las columnas requeridas
3. **Transformación** — lógica de negocio del área
4. **Salida** — exportar a Excel/CSV en `RUTA_SALIDA` o mostrar en consola

```python
def main() -> None:
    ...

if __name__ == "__main__":
    main()
```

## Convenciones

- Rutas siempre desde `config.py`, nunca hardcodeadas.
- Mensajes de error en español y accionables.
- Comentarios y docstrings en español.
- Variables de negocio en español cuando describen columnas del área.

## Al terminar

- Indicar el comando de prueba: `python scripts/nombre.py`
- Explicar en español qué hace cada parte relevante.
- Recordar que datos reales no se commitean al repo.

## Prompt del usuario (CRACO)

Si el pedido es vago, pedir o inferir:

- **Contexto**: qué archivo, qué columnas, qué regla de negocio
- **Acción**: filtrar, agrupar, calcular, exportar
- **Criterios**: manejo de filas vacías, validación de columnas
- **Output**: Excel, CSV, consola o SQLite
