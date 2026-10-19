"""Rutas del proyecto, siempre relativas a la raíz del repositorio.

Así los notebooks funcionan igual en cualquier ordenador y sistema operativo.
"""
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]

DATA = RAIZ / "data"
RAW = DATA / "raw"                  # CSV exportados del ERP y del MES (no se suben a git)
PROCESSED = DATA / "processed"      # tablas intermedias de los notebooks 01–09
MODELING = DATA / "modeling"        # partición temporal y folds (notebook 10)
PREDICTIONS = DATA / "predictions"  # predicciones de baselines y modelos (notebooks 11–14)

RESULTS = RAIZ / "results"
FIGURES = RESULTS / "figures"       # figuras para la memoria
TABLES = RESULTS / "tables"         # tablas resumen: embudo de depuración y métricas

for _carpeta in (PROCESSED, MODELING, PREDICTIONS, FIGURES, TABLES):
    _carpeta.mkdir(parents=True, exist_ok=True)
