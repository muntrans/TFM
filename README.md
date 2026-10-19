# Predicción de la desviación entre el tiempo teórico y el tiempo real en una planta de mecanizado

Trabajo Fin de Máster (Máster en Inteligencia Artificial).

Una planta de producción, el sistema ERP asigna a cada fase de fabricación un tiempo teórico. Otro sistema, el MES, registra el tiempo real que se dedica a ella. Este trabajo entrena modelos de aprendizaje automático que estiman, antes de ejecutar una fase, cuánto se desviará el tiempo real del teórico en la máquina asignada. La variable objetivo es el ratio entre el tiempo real efectivo y el tiempo teórico. El trabajo es predictivo: estima la desviación esperada de una asignación, no busca la asignación óptima.

## Resultado principal

Hipótesis: el modelo mejora en al menos un 20% el error (MAE) de la planificación actual del ERP (B0, ratio = 1).

| Referencia o modelo | MAE validación (media de 3 folds) | MAE test | Mejora frente a B0 en test |
|---|---:|---:|---:|
| B0 · planificación del ERP (ratio = 1) | 1,109 | 1,020 | – |
| B1 · mediana global del ratio | 0,974 | 0,905 | 11,3% |
| B2 · mediana del ratio por máquina | 0,933 | 0,863 | 15,4% |
| **LightGBM con log(ratio)** (modelo final) | **0,834** | **0,786** | **23%** |

El modelo final supera el umbral del 20 % en validación (24,7%) y en test (23%), así que la hipótesis se cumple. En minutos, el error medio por fase baja de 50,3 min (ERP) a 41,9 min. La comparación completa (Ridge, Random Foresty LightGBM, cada uno con ratio y con log(ratio)) está en `notebooks/15_evaluacion.ipynb` y en `results/tables/`.

## Estructura del repositorio

```
TFM_final/
├── README.md
├── requirements.txt
├── data/              → fuera de Git (ver data/README.md)
│   ├── raw/                → CSV exportados del ERP y del MES
│   ├── processed/          → tablas intermedias (notebooks 01–09)
│   ├── modeling/           → partición temporal y folds (notebook 10)
│   └── predictions/        → predicciones de baselines y modelos (notebooks 11–14)
├── notebooks/         → 00 a 15, en el orden en que se ejecutan
├── src/               → funciones que comparten los notebooks
├── results/           → resultados de los notebooks
│   ├── figures/            → figuras, con el número del notebook que las genera
│   └── tables/             → tablas de resultados (CSV)
├── sql/               → consulta de extracción de las imputaciones del MES
└── docs/              → diagramas y documentos
```

## Notebooks

| Notebook | Qué hace | Salida principal |
|---|---|---|
| `00_inventario_datos` | Describe las tablas en crudo y el reparto inicial de imputaciones | `results/tables/inventario_tablas.csv` |
| `01_imputaciones_limpieza` | Limpia las imputaciones del MES | `df_imputations_limpieza.parquet` |
| `02_maquinas_seleccion` | Selecciona las máquinas productivas y sus familias | `maquina_grupo.parquet` |
| `03_imputaciones_a_fases` | Agrupa las imputaciones en una fila por fase, con su tiempo real efectivo | `df_fases_MES.parquet` |
| `04_ordenes_fabricacion` | Filtra las órdenes de fabricación válidas | `df_OF.parquet` |
| `05_fases_erp_union_mes` | Limpia las fases del ERP y las une con las del MES | `df_FASE_final.parquet` |
| `06_articulos` | Añade la línea y la familia de producto del artículo | `df_final.parquet` |
| `07_viabilidad` | Comprueba que hay elección real de máquina dentro de cada familia | `results/tables/embudo_depuracion.csv` |
| `08_variable_objetivo` | Construye el ratio, corta los valores atípicos y lo analiza | `df_entrenamiento.parquet` |
| `09_seleccion_variables` | Elige las variables del modelo | `df_features.parquet` |
| `10_split_temporal` | Separa desarrollo y test por fecha y define los folds de validación | `df_split.parquet`, `folds.csv` |
| `11_baselines` | Calcula los baselines B0, B1 y B2 | `b0`, `b1`, `b2` |
| `12_ridge` | Regresión Ridge con ratio y con log(ratio) | `ridge_valid`, `ridge_test` |
| `13_random_forest` | Random Forest con ratio y con log(ratio) | `rf_valid`, `rf_test` |
| `14_lightgbm` | LightGBM con ratio y con log(ratio) | `lgbm_valid`, `lgbm_test` |
| `15_evaluacion` | Selecciona el modelo, lo evalúa en test y lo interpreta con SHAP | `results/tables/`, `results/figures/` |

Cada notebook empieza con su objetivo, su entrada y su salida. Los hiperparámetros se eligen solo con validación (3 folds temporales dentro del conjunto de desarrollo). El test se evalúa una única vez, en el notebook 15.

## Cómo reproducir los resultados

Probado con Python 3.13. En Windows (PowerShell), desde la carpeta del repositorio:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

1. Sin los CSV en crudo en `data/raw/` no es posible ejecutar el codigo al completo desde el principio. 
2. Ejecuta los notebooks en orden, del 00 al 15, cada uno con *Restart & Run All*. También se pueden ejecutar todos seguidos desde la terminal:

```powershell
Get-ChildItem notebooks\*.ipynb | Sort-Object Name | ForEach-Object { jupyter nbconvert --to notebook --execute --inplace $_.FullName }
```

Cada notebook lee lo que escribe el anterior, así que también se puede volver a ejecutar uno suelto si existen sus entradas. Para los modelos las semillas están fijadas y los resultados se repiten. 

## Datos

Los datos son registros reales de la planta y no se incluyen en el repositorio. En `data/README.md` está la lista de tablas, su formato y cómo se obtuvieron.


## Documentación

- `docs/diagramas/`: relación entre el ERP y el MES (`MES+ERP.drawio`, `ERP+MES.png`) y esquema de la limpieza de
  datos (`Diagrama_Inspección.drawio`).
- `docs/Declaracion_uso_IA.docx`: declaración de uso de herramientas de IA.
