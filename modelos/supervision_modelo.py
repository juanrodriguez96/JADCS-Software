from pydantic import BaseModel

class SupervisionIn(BaseModel):
    idJefe:       str
    idEmpleado:   str
	
class SupervisionOut(BaseModel):
    idJefe:       str
