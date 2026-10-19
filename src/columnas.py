"""Nombres de columna de las tablas exportadas del ERP y del MES.

Los CSV en crudo se exportaron sin fila de cabecera, así que los nombres de
columna se definen aquí, en un único sitio, y se aplican al leerlos.
"""
import pandas as pd

from src.rutas import RAW


def leer_csv(archivo, columnas):
    """Lee un CSV de data/raw (separador ';' y sin cabecera) con sus nombres de columna.

    low_memory=False hace que pandas deduzca el tipo de cada columna con el
    archivo completo, lo que evita los avisos DtypeWarning de tipos mezclados.
    """
    return pd.read_csv(RAW / archivo, sep=";", header=None, names=columnas, low_memory=False)


# MES · imputaciones de tiempo (imputaciones.csv)
COLUMNAS_IMPUTACIONES = [
    "FechaCreacionDte", "smNodoId", "smNodoNme", "smOrdenId", "smMaterialId",
    "smOrdenNme", "smFaseId", "smFaseNme", "CantidadManualOKNbr",
    "CantidadManualNOKNbr", "MinutosRealNbr", "MinutosPreparacionNbr",
    "MinutosProduccionNbr", "PorcentajeDedicacionNbr", "ProductivoInd",
    "smIncidenciaId", "smIncidenciaNme", "smFasePersonalizado1Txt", "smNodoId2",
    "smNodoPersonalizado1Nbr", "smNodoPersonalizado2Nbr", "ssEnumFaseEstadoId",
    "SmFaseUid", "TraspasadoInd", "JsonBodyTxt", "JsonResponseTxt",
]

# MES · nodos de captura: máquinas y puestos (SmNodo.csv)
COLUMNAS_NODOS = [
    "SmNodoUid", "smNodoId", "smNodoCodigoGestion", "smNodoNme", "smNodoDsc",
    "smEstructuraUid", "padre_smNodoUid", "presenciaEnPlantaInd",
    "smNodoPersonalizado1Dte", "smNodoPersonalizado2Dte", "smNodoPersonalizado1Nbr",
    "smNodoPersonalizado2Nbr", "smNodoPersonalizado1Txt", "smNodoPersonalizado2Txt",
    "EsMaquinaOlanetInd", "bajaInd", "guardarTimestampPiezaInd",
    "FechaUltimaActualizacionDte", "Planta", "modificadoPor_usuario_guid",
    "FechaCreacionDte", "Ortems_smNodoPersonalizado1Txt",
    "Ortems_smNodoPersonalizado2Txt", "ssEnumTipoVerticalId",
]

# MES · correspondencia de identificadores ERP–MES (maping_fase.csv)
COLUMNAS_MAPEO = [
    "SmERPEntityMappingUid", "ERPEntityType", "ERPEntityId", "MESEntityType",
    "MESEntityId", "bajaInd", "FechaUltimaActualizacionDte", "Planta",
    "modificadoPor_usuario_guid", "FechaCreacionDte",
]

# ERP · fases de las órdenes de fabricación (CPRMOTask.csv)
COLUMNAS_FASES = [
    "IDMOTask", "CodCompany", "IDManufacturingOrder", "CodMOTask", "Description",
    "Notes", "Order", "PreparationTime", "ExecutionTime", "RepetitionTime", "TimeUnit",
    "ProductEntry", "MaterialExit", "DelimitationType", "DelimitationDate",
    "AllowFraccionate", "MinimumFraction", "IDUsualTask", "TaskType", "IDMOTaskParent",
    "RepetitionLot", "External", "IDArticleExternal", "Quantity", "IDSupplier",
    "IDTaskType", "RepetitionTimeReal", "PlannedStartDate", "PlannedEndDate", "Group",
    "IDTask", "PercentProgress", "SeriesRequired", "QualityStatus", "InspectedDate",
    "Priority", "OptimizationFeature", "Fixed", "WithoutTimetable", "OccupancyType",
    "OccupancyHours", "OccupancyPercent", "ManualEndDate", "ManualStartDate", "Blocked",
    "DelimitationObligatory", "IDBudgetCategory", "ResourcePlanType", "SplitNumber",
    "ManualPlanning", "IDBudgetEmployee", "IDBudgetMachine", "IDBudgetTool",
    "IDBudgetMaterial", "IDBudgetOtherCost", "RowTimestamp", "WorkUnits",
    "LastModifiedBy", "IDProductFormula", "DateReplanify", "LotsOrder", "PrintLabels",
    "AutoExecutionImputation", "IDSiteMaterial", "IDWarehouseMaterial",
    "GroupingNumber", "CreationTimestamp", "RowCreatedBy", "BlockedMaterial",
    "BlockedCost", "ImputationCostUpdated", "Canceled", "RealEndDate", "IDCheckList",
    "NotOverlapCode", "TiedCode", "GroupedManufacturing", "ReleaseKeptResources",
    "DelayMargin", "BlockedChangeMaterial", "IDHourType", "Color",
    "SetToQtyConversionFactor", "AdjustTaskToDay", "PercentProgressType",
    "StatusTaskMES",
]

# ERP · órdenes de fabricación (CPRManufacturingOrder.csv)
COLUMNAS_OF = [
    "IDManufacturingOrder", "CodCompany", "CodManufacturingOrder", "IDArticle",
    "IDStructure", "Description", "TimeUnitDefault", "IDStructureType", "Notes",
    "Quantity", "IDWareHouse", "PlannedEndDate", "PlannedStartDate",
    "PlannedEndMRPDate", "ManualEndDate", "Priority", "IDMOSituation", "Color", "Group",
    "InternalCode", "IDRoute", "AcceptedDate", "RealEndDate", "IDProject", "IDProTask",
    "IDProMaterial", "AutomaticCodification", "ManualPStartDate", "ManualPEndDate",
    "IDSite", "Historic", "RowTimestamp", "PlanningDirection", "LastModifiedBy",
    "QuantityBaseFormula", "IDUnitBaseFormula", "IDArticleVersion", "CreationTimestamp",
    "RowCreatedBy", "IDMaintenanceOrder", "IDOrderMaterialPrevision", "IDLaunchedMRP",
    "AutoBatchAssignSalesOrders",
]

# ERP · máquinas (CPRMachine.csv)
COLUMNAS_MAQUINAS = [
    "IDMachine", "CodCompany", "CodMachine", "Description", "CostType", "IDMeasureUnit",
    "BottleNeck", "Image", "IDCalendar", "PosX", "PosY", "Fictitious", "InactivateDate",
    "IDSite", "RowTimestamp", "LastModifiedBy", "ImputationOnLineUnique",
    "AllowMultiImputation", "CreationTimestamp", "RowCreatedBy", "DisplayOrder",
]

# ERP · grupos de máquinas (CPRMachineGroup.csv)
COLUMNAS_GRUPOS = [
    "IDMachineGroup", "CodCompany", "CodMachineGroup", "Description", "Infinite",
    "IDCalendar", "IDSite", "RowTimestamp", "BottleNeck", "LastModifiedBy",
    "KeepResource", "CreationTimestamp", "RowCreatedBy", "CalendarType",
]

# ERP · pertenencia de cada máquina a su grupo (CPRMachineGroupElement.csv)
COLUMNAS_MAQUINA_GRUPO = [
    "IDMachineGroupElement", "CodCompany", "IDMachineGroup", "IDMachine", "Priority",
    "Alternative", "RowTimestamp", "LastModifiedBy", "CreationTimestamp", "RowCreatedBy",
]

# ERP · artículos (STKArticle.csv)
COLUMNAS_ARTICULOS = [
    "IDArticle", "CodCompany", "CodArticle", "Description", "Image", "Notes",
    "LocationWarehouseControl", "SeriesControl", "UnitarianSeries", "ExpiryControl",
    "ExpireDays", "IDUnitQuantityWarehouse", "IDUnitPriceWarehouse", "SecondUnit",
    "IDUnitSecondUnit", "IDUnitQuantityPurchase", "IDUnitPricePurchase",
    "IDProductLine", "IDProductFamily", "IDProductSubFamily", "StatisticsCode",
    "CodCountryOfOrigin", "SupplemetUnit", "IDUnitSupplement", "AverageSecondUnit",
    "Dimension", "ApplyPurchaseDiscount", "ApplyPurFinancialSurcharge", "IDAttribute1",
    "IDAttribute2", "IDAttribute3", "IDAttributeValue1", "IDAttributeValue2",
    "IDAttributeValue3", "IDArticleGeneric", "CodArticlePrevious",
    "IDUnitHomogeneousPurchase", "PlanningCategory", "PlanningGroup", "GroupDays",
    "NetWeight", "MakeAutomaticOutput", "ImputationCostUpdated", "InvestmentExpense",
    "IDUnitQuantitySales", "IDUnitPriceSales", "ApplySalesDiscount",
    "ApplySalesFinancialSurcharge", "IDUnitHomogeneousSales", "AverageSecondUnitSerie",
    "GrossWeight", "Container", "HasContainer", "DiscountContainer", "IDStatusLotGroup",
    "StatusLot", "ConsumePrevisionBehavior", "PDMItemID", "ImputationTotalQuantity",
    "GroupDaysNumber", "TechnicalDescription", "MRPPrevisionsOnly",
    "ApplySalesRetention", "ApplyPurchaseRetention", "RowTimestamp", "LastModifiedBy",
    "QuantityBaseFormula", "IDUnitBaseFormula", "PotencyControl", "PotencyDefault",
    "BatchBalancing", "MultipleCADLink", "ComponentsGroupType", "InactiveDate",
    "WholeSeries", "LotsReserve", "LotsReserveDays", "LotsOrder", "LotsOrderDays",
    "SecondUnitFixed", "MatchCode", "UnitarianSerieOrder", "IDArticleContainer",
    "CreationTimestamp", "RowCreatedBy", "ApplyCommission", "ApplySalesDiscountPP",
    "ApplyPurchaseDiscountPP", "IDArticleClassification", "ManufacturingGroupCode",
    "ManufacturingGroupQuantity", "MaterialPreparationType", "NotBillablePurchase",
    "NotBillableSales", "NotApplyNetWeightNetMass", "UDI", "UDIBasic", "HSCode",
]

# ERP · líneas de producto (ProductLine.csv)
COLUMNAS_LINEAS = [
    "IDProductLine", "CodCompany", "CodProductLine", "Description", "Image",
    "RowTimestamp", "LastModifiedBy", "CreationTimestamp", "RowCreatedBy",
]

# ERP · familias de producto (ProductFamily.csv)
COLUMNAS_FAMILIAS = [
    "IDProductFamily", "CodCompany", "IDProductLine", "CodProductFamily", "Description",
    "Image", "RowTimestamp", "LastModifiedBy", "CreationTimestamp", "RowCreatedBy",
]
