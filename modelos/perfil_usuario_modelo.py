from pydantic import BaseModel

class personaIn(BaseModel):
    idUsuario:      int
    contrasenia:	str
	
class personaOut(BaseModel):
    nombre:			str
    apellido:		str
    categoria:		str
