# Stack 1 — Guía del repositorio

Repositorio base del piloto para construir scripts de datos con Cursor como copiloto. No incluye código de ejemplo: el desarrollo lo genera cada área con IA sobre esta base.

## Stack permitido

| Componente | Tecnología |
|------------|------------|
| Runtime | Python 3.11+ |
| Datos | pandas, openpyxl |
| Visualización | streamlit, plotly (cuando el área necesite un visor) |
| Base de datos | sqlite3 (stdlib); PostgreSQL solo con aprobación de IT |

Dependencias en `requirements.txt`. No agregar librerías nuevas sin consultar IT.

## Estructura de carpetas

```
.
├── .cursor/
│   ├── rules/             # Reglas permanentes (stack1.mdc)
│   └── skills/            # Skills del proyecto (compartidas al clonar)
├── config.py              # Rutas y parámetros del área
├── scripts/               # Scripts que crea el consultor (ETL, procesos, utilidades)
├── data/                  # Datos locales (no commitear archivos reales)
├── .cursorrules           # Reglas permanentes para Cursor
└── requirements.txt       # Dependencias aprobadas
```

### config.py

Centraliza rutas a archivos de entrada y salida. Los datos reales del área van en rutas locales configuradas aquí, nunca hardcodeadas en los scripts.

### scripts/

Cada script del área vive aquí. Convención sugerida: un archivo por tarea (`leer_datos.py`, `procesar.py`, etc.).

### data/

Carpeta local para archivos de entrada y salida. Está en `.gitignore` salvo el marcador `.gitkeep`. No subir Excel, CSV ni bases de datos reales al repositorio.

## Reglas de Cursor

El archivo `.cursorrules` en la raíz define cómo debe comportarse la IA en este proyecto:

- Comentarios y mensajes en español.
- Sin credenciales ni datos sensibles en el código ni en el chat.
- Rutas en `config.py`.
- Manejo de errores al leer archivos o bases de datos.
- Funciones cortas: separar carga, transformación y salida.
- Explicar cambios y cómo probarlos.

También existe `.cursor/rules/stack1.mdc` con las mismas reglas en formato moderno de Cursor.

Para reglas propias del área, agregarlas al final de `.cursorrules` sin eliminar las de IT.

## Skills de Cursor

Las **skills de proyecto** viven en `.cursor/skills/` y se comparten con todos al clonar el repo. No hace falta que cada persona las instale por su cuenta.

| Skill | Cuándo la usa Cursor |
|-------|----------------------|
| `crear-script-datos` | Crear o modificar scripts en `scripts/`, procesar Excel/CSV |
| `resolver-errores-python` | Corregir tracebacks, columnas faltantes, archivos no encontrados |

Cursor las detecta automáticamente según lo que pidas en el chat. También podés invocarlas mencionando la tarea (por ejemplo: "creá un script que lea el Excel del área").

Las skills **personales** (`~/.cursor/skills/`) son opcionales y las configura cada usuario en su máquina. Las de este repo ya cubren el flujo del Stack 1.

Para reglas de negocio propias del área, agregar una skill en `.cursor/skills/nombre-del-area/SKILL.md` o ampliar `.cursorrules`.

## Flujo de trabajo con Cursor

1. Abrir la carpeta del proyecto en Cursor.
2. Describir en español qué debe hacer el script (lógica de negocio, columnas, filtros).
3. Pedir a Cursor que cree o modifique archivos en `scripts/`.
4. Revisar el diff antes de aceptar cambios.
5. Ejecutar desde la terminal integrada: `python scripts/nombre.py`.
6. Si hay error, pegar el traceback completo en el chat.

### Atajos útiles

| Atajo | Uso |
|-------|-----|
| `Ctrl+L` | Chat — preguntas y explicaciones |
| `Ctrl+K` | Edición inline — cambio puntual |
| `Ctrl+I` | Composer — tareas en varios archivos |
| `@archivo` | Referenciar un archivo en el chat |

## Seguridad

- No commitear `.env`, Excel, CSV ni bases de datos con datos reales.
- Usar `.env.example` como referencia si IT habilita PostgreSQL.
- No pegar contraseñas ni datos personales en el chat de Cursor.

## Cuándo usar cada almacenamiento

| Opción | Uso |
|--------|-----|
| Excel / CSV | Entrada y salida del área |
| SQLite | Historial o prototipos en local, sin servidor |
| PostgreSQL | Datos compartidos entre varios usuarios (con IT) |

## Personalización por área

Al iniciar el proyecto:

1. Renombrar o actualizar el README con el nombre de la herramienta del área.
2. Configurar `config.py` con las rutas reales.
3. Agregar reglas de negocio al final de `.cursorrules`.
4. Crear el primer script en `scripts/` con Cursor.
