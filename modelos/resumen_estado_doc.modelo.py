from pydantic import BaseModel
from datetime import datetime



class DocumentoIn(BaseModel):
    username: str
    tip: str

class DocumentoOut(BaseModel):
    id_radicado: int
    username: str
    date_up: datetime
    tip: str
    status: str