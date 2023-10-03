# ServicioModel: 

##########################################

from pydantic import BaseModel

##########################################

class ModeloServicio(BaseModel):
	NombreProducto: str | None = None
	TipoProducto: str | None = None
	Precio: str | None = None
	
##########################################