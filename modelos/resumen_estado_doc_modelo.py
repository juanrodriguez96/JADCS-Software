from pydantic import BaseModel
from datetime import date


class DocumentoIn(BaseModel):
    id_radicado: str
    fecha_radicacion: date
    fecha_asignacion: date = date.today()
    fecha_vencimiento: date
    tipo: str
    status: str
    anexos: int = 0


class DocumentoOut(BaseModel):
    id_radicado: str
    username: str
    fecha_asignacion: date
    status: str

class DocumentoBorrar(BaseModel):
    idUsuario: str
    id_radicado: int