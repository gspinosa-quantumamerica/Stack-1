"""
Configuración del proyecto.

Ajustar rutas y parámetros según el área. Los datos reales no deben commitearse.
"""

from pathlib import Path

PROYECTO_ROOT = Path(__file__).resolve().parent

# Ruta al Excel o CSV de entrada (cambiar por tu archivo local)
RUTA_DATOS_ENTRADA = PROYECTO_ROOT / "data" / "entrada.csv"

# Carpeta de salida para exports
RUTA_SALIDA = PROYECTO_ROOT / "data"
