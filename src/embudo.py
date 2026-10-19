"""Registro del embudo de depuración: cuántas filas quedan tras cada filtro.

Cada notebook de preparación guarda su embudo en results/tables/embudo_NN.json
(legible en GitHub) y el notebook 07 los reúne.
"""
import json

import pandas as pd

from src.rutas import TABLES


def guardar_embudo(embudo, nombre):
    """Guarda el diccionario {paso: número} en results/tables/embudo_<nombre>.json."""
    datos = {paso: int(n) for paso, n in embudo.items()}
    ruta = TABLES / f"embudo_{nombre}.json"
    ruta.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")


def cargar_embudo(nombre):
    """Lee el embudo guardado por un notebook de preparación."""
    ruta = TABLES / f"embudo_{nombre}.json"
    return json.loads(ruta.read_text(encoding="utf-8"))


def tabla_embudo(embudo, unidad="Número"):
    """Convierte el embudo en una tabla de una columna para mostrarla."""
    return pd.Series(embudo, name=unidad).to_frame()
