from pydantic import BaseModel


class personaIn(BaseModel):
    idUsuario:      str
    contrasenia:	str


class personaOut(BaseModel):
    nombre:			str
    apellido:		str
    categoria:		str
