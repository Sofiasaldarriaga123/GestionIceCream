# UsuarioModel: 

##########################################

from pydantic import BaseModel

##########################################

class ModeloUsuario(BaseModel):
	NombreCliente: str | None = None
	ApellidoCliente: str | None = None
	Correo: str | None = None
	Telefono: str | None = None
	NombreGenero: str | None = None
	
##########################################