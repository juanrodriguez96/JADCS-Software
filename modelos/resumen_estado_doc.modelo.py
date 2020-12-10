from pydantic import BaseModel
from datetime import datetime


class DocumentoIn(BaseModel):
    id_radicado: str
    username: str
    fecha_asignacion: datetime
    status: str


class DocumentoOut(BaseModel):
    id_radicado: str
    username: str
    fecha_asignacion: datetime
    status: str
