"""Funciones de limpieza que se repiten en los notebooks de preparación (01–06)."""
import pandas as pd
import numpy as np


def eliminar_columnas(df, columnas):
    """Devuelve una copia de df sin las columnas indicadas.

    Avisa de las columnas de la lista que no existen en la tabla (por si hay
    una errata o un nombre distinto) e informa de cuántas columnas quedan.
    """
    presentes = [c for c in columnas if c in df.columns]
    ausentes = [c for c in columnas if c not in df.columns]
    if ausentes:
        print(f"Aviso: {len(ausentes)} columnas de la lista no están en la tabla: {ausentes}")
    df_out = df.drop(columns=presentes)
    print(f"Eliminadas {len(presentes)} columnas. Quedan {df_out.shape[1]} columnas y {df_out.shape[0]} filas.")
    return df_out


def filtrar_por_fecha(df, columna, desde=None, hasta=None, unidad="filas"):
    """Conserva las filas con fecha entre `desde` y `hasta` (ambos incluidos).

    La columna se convierte a fecha; los valores no interpretables pasan a NaT
    y quedan fuera del filtro, con un aviso.
    """
    df_out = df.copy()
    df_out[columna] = pd.to_datetime(df_out[columna], errors="coerce")
    n_nat = df_out[columna].isna().sum()
    if n_nat:
        print(f"Aviso: {n_nat} {unidad} con fecha no interpretable quedan fuera del filtro.")

    print(f"Partida: {len(df_out)} {unidad}")
    if desde is not None:
        antes = len(df_out)
        df_out = df_out[df_out[columna] >= pd.to_datetime(desde)]
        print(f"Desde {desde}: {len(df_out)} (descartadas {antes - len(df_out)})")
    if hasta is not None:
        antes = len(df_out)
        df_out = df_out[df_out[columna] <= pd.to_datetime(hasta)]
        print(f"Hasta {hasta}: {len(df_out)} (descartadas {antes - len(df_out)})")
    return df_out.copy()



def corte_log(df, k=1.5):
    """
    Devuelve los umbrales de ratio (bajo y alto)  
    """
    log_ratio = np.log(df["ratio"])
    q1, q3 = log_ratio.quantile([0.25, 0.75])
    iqr = q3 - q1
    umbral_bajo = np.exp(q1 - k * iqr).round(3)
    umbral_alto = np.exp(q3 + k * iqr).round(3)
    print(f"Umbrales: {umbral_bajo} (bajo) y {umbral_alto} (alto)")

    return umbral_bajo, umbral_alto