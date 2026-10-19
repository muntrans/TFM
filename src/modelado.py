"""Funciones comunes de los notebooks de modelado (10–15).

Reúne la carga de datos, las métricas, la partición por folds y el bucle
"entrenar en cada fold y medir", que antes estaba copiado en cada notebook.
"""
import numpy as np
import pandas as pd

from src.rutas import MODELING

VARIABLES_CATEGORICAS = ["CodigoMaquina", "Familia Maquinas", "TipoFase",
                         "Línea Producto", "Família Producto"]
VARIABLES_NUMERICAS = ["TiempoPrevisto", "Quantity"]
VARIABLES = VARIABLES_CATEGORICAS + VARIABLES_NUMERICAS
OBJETIVO = "ratio"

# Configuración final de LightGBM, fijada con validación en el notebook 14
CONFIG_LGBM_FINAL = dict(num_leaves=15, min_child_samples=10, n_estimators=500,
                         learning_rate=0.05, random_state=42, verbose=-1)


def cargar_datos_modelado():
    """Devuelve el dataset con la partición temporal y la lista de meses de validación."""
    df = pd.read_parquet(MODELING / "df_split.parquet")
    folds = pd.read_csv(MODELING / "folds.csv", dtype=str)
    return df, folds["mes_validacion"].tolist()


def rellenar_desconocidas(df):
    """Etiqueta como 'Desconocida' la línea y la familia de producto que faltan."""
    df = df.copy()
    for col in ["Línea Producto", "Família Producto"]:
        df[col] = df[col].fillna("Desconocida")
    return df


def preparar_para_lightgbm(df):
    """Convierte las variables categóricas al tipo 'category' que LightGBM trata de forma nativa."""
    df = df.copy()
    df[VARIABLES_CATEGORICAS] = df[VARIABLES_CATEGORICAS].astype("category")
    return df


def metricas(y_real, y_pred):
    """MAE, RMSE y número de fases."""
    error = y_pred - y_real
    return {"MAE": np.abs(error).mean(),
            "RMSE": np.sqrt((error ** 2).mean()),
            "n": len(y_real)}


def obtener_fold(df, mes_val):
    """Devuelve (train, valid) de un fold temporal dentro de desarrollo.

    Train: meses de desarrollo anteriores a mes_val. Valid: el propio mes_val.
    """
    desarrollo = df[df["split"] == "desarrollo"]
    train = desarrollo[desarrollo["mes_orden"] < mes_val]
    valid = desarrollo[desarrollo["mes_orden"] == mes_val]
    return train, valid


def bloques_evaluacion(df, meses):
    """Recorre los bloques de evaluación: los folds de validación y, al final, el test.

    Devuelve (nombre, train, evaluar). En test se entrena con todo desarrollo.
    """
    for mes in meses:
        train, valid = obtener_fold(df, mes)
        yield f"valid {mes}", train, valid
    yield "test", df[df["split"] == "desarrollo"], df[df["split"] == "test"]


def ajustar_y_predecir(modelo, train, evaluar, log=False, columnas=VARIABLES):
    """Entrena con `train` y predice `evaluar`, siempre en escala ratio.

    Con log=True el modelo aprende log(ratio) y la predicción se devuelve a
    escala ratio con la exponencial.
    """
    y = np.log(train[OBJETIVO]) if log else train[OBJETIVO]
    modelo.fit(train[columnas], y)
    pred = modelo.predict(evaluar[columnas])
    return np.exp(pred) if log else pred


def evaluar_en_folds(modelo, df, meses, log=False, columnas=VARIABLES, con_train=False):
    """Entrena y valida el modelo en cada fold temporal.

    Devuelve dos tablas: las métricas por fold y las predicciones fase a fase.
    Con con_train=True también calcula el MAE en entrenamiento (sobreajuste).
    """
    filas, partes = [], []
    for mes in meses:
        train, valid = obtener_fold(df, mes)
        pred = ajustar_y_predecir(modelo, train, valid, log, columnas)
        fila = {"bloque": f"valid {mes}", "n_train": len(train)}
        if con_train:
            pred_train = modelo.predict(train[columnas])
            pred_train = np.exp(pred_train) if log else pred_train
            fila["MAE_train"] = metricas(train[OBJETIVO], pred_train)["MAE"]
        fila.update(metricas(valid[OBJETIVO], pred))
        filas.append(fila)
        partes.append(pd.DataFrame({"IDMOTask": valid["IDMOTask"].values,
                                    "mes_orden": valid["mes_orden"].values,
                                    OBJETIVO: valid[OBJETIVO].values,
                                    "pred": pred}))
    return pd.DataFrame(filas), pd.concat(partes, ignore_index=True)


def buscar_hiperparametros(modelo, rejilla, df, meses, log=False, columnas=VARIABLES):
    """Prueba cada combinación de `rejilla` (lista de diccionarios) con los folds temporales."""
    filas = []
    for params in rejilla:
        modelo.set_params(**params)
        res, _ = evaluar_en_folds(modelo, df, meses, log, columnas, con_train=True)
        filas.append({**params,
                      "MAE_train": res["MAE_train"].mean(),
                      "MAE_medio_val": res["MAE"].mean(),
                      "RMSE_medio": res["RMSE"].mean(),
                      "MAE_por_fold": res["MAE"].round(3).tolist()})
    return pd.DataFrame(filas)
