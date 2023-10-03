# OrganizacionModel: 

##########################################

from pydantic import BaseModel

##########################################

class ModeloOrganizacion(BaseModel):
	NitEmpresa: str | None = None
	NombreEmpresa: str | None = None
	NombreSede: str | None = None
	DireccionSede: str | None = None
	DocumentoVendedor: str | None = None
	NombreVendedor: str | None = None
	ApellidoVendedor: str | None = None
	
##########################################