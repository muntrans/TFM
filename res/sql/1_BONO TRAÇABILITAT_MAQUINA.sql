--** BONO MAQUINA/CENTRE TREBALL **

SELECT   
ShNodoFaseTiempoMaterialSalidaCantidad.FechaCreacionDte, 
SmNodo.smNodoId,
smNodo.smNodoNme,
SmOrden.smOrdenId,
SmMaterial.smMaterialId, 
SmOrden.smOrdenNme, 
SmFase.smFaseId,
SmFase.smFaseNme,
ShNodoFaseTiempoMaterialSalidaCantidad.CantidadManualOKNbr, 
ShNodoFaseTiempoMaterialSalidaCantidad.CantidadManualNOKNbr,
ShNodoFaseTiempoMaterialSalidaCantidad.MinutosRealNbr, 
ShNodoFaseTiempoMaterialSalidaCantidad.MinutosPreparacionNbr, 
ShNodoFaseTiempoMaterialSalidaCantidad.MinutosProduccionNbr, 
ShNodoFaseTiempoMaterialSalidaCantidad.PorcentajeDedicacionNbr, 
ShNodoFaseTiempoMaterialSalidaCantidad.ProductivoInd, 
SmIncidencia.smIncidenciaId,
SmIncidencia.smIncidenciaNme,
smfase.smFasePersonalizado1Txt,
SmNodo.smNodoId,
SmNodo.smNodoPersonalizado1Nbr, 
SmNodo.smNodoPersonalizado2Nbr,
SmFase.ssEnumFaseEstadoId, 
smfase.SmFaseUid,
ShNodoFaseTiempoMaterialSalidaCantidad.TraspasadoInd,
ShNodoFaseTiempoMaterialSalidaCantidad.JsonBodyTxt,
ShNodoFaseTiempoMaterialSalidaCantidad.JsonResponseTxt

FROM            ShNodoFaseTiempoMaterialSalidaCantidad LEFT OUTER JOIN
                         
                         SmFase ON ShNodoFaseTiempoMaterialSalidaCantidad.smFaseUid = SmFase.SmFaseUid LEFT OUTER JOIN
                         SmOrden ON SmFase.smOrdenUid = SmOrden.SmOrdenUid LEFT OUTER JOIN
                         SmFaseMaterialSalida ON SmFase.SmFaseUid = SmFaseMaterialSalida.smFaseUid LEFT OUTER JOIN
                         SmMaterial ON SmFaseMaterialSalida.smMaterialUid = SmMaterial.SmMaterialUid LEFT OUTER JOIN
                         SmNodo ON ShNodoFaseTiempoMaterialSalidaCantidad.smNodoUid = SmNodo.SmNodoUid LEFT OUTER JOIN
                         SmIncidencia ON ShNodoFaseTiempoMaterialSalidaCantidad.smIncidenciaUid = SmIncidencia.SmIncidenciaUid 
                       

						 order by ShNodoFaseTiempoMaterialSalidaCantidad.FechaCreacionDte desc