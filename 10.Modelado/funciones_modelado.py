# funciones_modelado.py
import numpy as np
import pandas as pd

def metricas(y_real, y_pred):
    error = y_pred - y_real
    return {"MAE":  np.abs(error).mean(),
            "RMSE": np.sqrt((error ** 2).mean()),
            "n":    len(y_real)}

def obtener_fold(df, mes_val):
    """
    Devuelve (train, valid) de un fold temporal.
    mes_val supone el punto de corte:
        anterior a mes_val = train
        posterior a mes_val = validación 
    """
    desarrollo = df[df["split"] == "desarrollo"]
    train = desarrollo[desarrollo["mes_orden"] < mes_val]
    valid = desarrollo[desarrollo["mes_orden"] == mes_val]
    return train, valid