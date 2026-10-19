# Datos

Los datos son registros reales de la planta, exportados del ERP y del MES. Son confidenciales y no se suben al repositorio: `.gitignore` excluye el contenido de las cuatro carpetas de `data/`.

| Carpeta | Contenido | Quién lo crea |
|---|---|---|
| `raw/` | CSV exportados del ERP y del MES. No se modifican nunca. | Exportación manual |
| `processed/` | Tablas intermedias de la preparación de datos (parquet) | Notebooks 01 a 09 |
| `modeling/` | Dataset con la partición temporal y los folds de validación | Notebook 10 |
| `predictions/` | Predicciones de los baselines y de los modelos, fase a fase | Notebooks 11 a 14 |

## Datos en crudo (`raw/`)

Para ejecutar el proyecto desde cero hay que copiar en `raw/` estos once archivos.

| Archivo | Sistema | Contenido | Filas | Columnas | Se usa en |
|---|---|---|---:|---:|---|
| `imputaciones.csv` | MES | Imputaciones de tiempo en cada máquina y fase | 196.576 | 26 | 01 |
| `SmNodo.csv` | MES | Nodos de captura: máquinas y puestos de trabajo | 119 | 24 | 02 |
| `maping_fase.csv` | MES | Correspondencia de identificadores de fase ERP–MES | 118.997 | 10 | 05 |
| `CPRMachine.csv` | ERP | Máquinas | 145 | 21 | 02 |
| `CPRMachineGroup.csv` | ERP | Grupos (familias) de máquinas | 61 | 14 | 02 |
| `CPRMachineGroupElement.csv` | ERP | Pertenencia de cada máquina a su grupo | 130 | 10 | 02 |
| `CPRManufacturingOrder.csv` | ERP | Órdenes de fabricación (OF) | 18.106 | 43 | 04 |
| `CPRMOTask.csv` | ERP | Fases de las OF, con su tiempo teórico | 116.055 | 86 | 05 |
| `STKArticle.csv` | ERP | Artículos | 57.880 | 98 | 06 |
| `ProductLine.csv` | ERP | Líneas de producto | 18 | 9 | 06 |
| `ProductFamily.csv` | ERP | Familias de producto | 82 | 10 | 06 |

Formato: separador `;` y sin fila de cabecera. Los nombres de las columnas están en `src/columnas.py`, y la función
`leer_csv` de ese mismo archivo es la que se usa para leerlos.

`imputaciones.csv` es el resultado de la consulta `sql/imputaciones_mes.sql`. Cada uno de los demás archivos
corresponde a una tabla del ERP o del MES con el mismo nombre.

## Tablas intermedias (`processed/`)

| Archivo | Lo crea | Contenido |
|---|---|---|
| `df_imputations_limpieza.parquet` | 01 | Imputaciones limpias |
| `maquina_grupo.parquet` | 02 | Máquinas productivas y su familia |
| `df_fases_MES.parquet` | 03 | Una fila por fase del MES, con su tiempo real |
| `df_OF.parquet` | 04 | Órdenes de fabricación válidas |
| `df_FASE_final.parquet` | 05 | Fases del ERP unidas con las del MES |
| `df_final.parquet` | 06 | Fases con los datos del artículo |
| `df_entrenamiento.parquet` | 08 | Fases con la variable objetivo, tras el corte de valores atípicos |
| `df_features.parquet` | 09 | Variables del modelo |

## Modelado (`modeling/` y `predictions/`)

- `modeling/df_split.parquet` y `modeling/folds.csv`: partición temporal (desarrollo y test) y meses de validación.
- `predictions/b0.parquet`, `b1.parquet` y `b2.parquet`: predicciones de los baselines.
- `predictions/<modelo>_valid.parquet` y `<modelo>_test.parquet`: predicciones de Ridge, Random Forest y LightGBM en
  validación y en test.

Las carpetas `processed/`, `modeling/` y `predictions/` se crean solas al ejecutar los notebooks (`src/rutas.py`).
