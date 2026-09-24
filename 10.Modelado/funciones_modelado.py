# funciones_modelado.py
import numpy as np
import pandas as pd

def metricas(y_real, y_pred):
    error = y_pred - y_real
    return {"MAE":  np.abs(error).mean(),
            "RMSE": np.sqrt((error ** 2).mean()),
            "n":    len(y_real)}

def obtener_fold(df, mes_val):
    """Devuelve (train, valid) de un fold temporal.
    train = desarrollo anterior a mes_val · valid = OF iniciadas en mes_val"""
    desarrollo = df[df["split"] == "desarrollo"]
    train = desarrollo[desarrollo["mes_orden"] < mes_val]
    valid = desarrollo[desarrollo["mes_orden"] == mes_val]
    return train, valid