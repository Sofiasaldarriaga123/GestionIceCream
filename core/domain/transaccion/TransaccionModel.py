# TransaccionModel: 

##########################################

from pydantic import BaseModel

##########################################

class ModeloTransaccion(BaseModel):
	NombreVenta: str | None = None
	Fecha: str | None = None
	Cantidad: str | None = None
	Total: str | None = None
	
##########################################