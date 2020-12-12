from typing import  Dict
from pydantic import BaseModel

class Supervision(BaseModel):
	idJefe:		str
	idEmpleado:	str

database_Supervision = Dict[str, str]


database_Supervision = {
	"andres18":"camilo24",
	"robin":"batman",
	"batgirl":"batman"
}

def getSupervision(jefe : str):
	emp =[]
	for k,v in database_Supervision.items():
		if v==jefe:	
			emp.append(k)

	return emp

def updateSupervision (jefe: str, nojefe:str):
	database_Supervision[nojefe] = jefe
	return jefe
