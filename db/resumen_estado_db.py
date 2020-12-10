from datetime import datetime
from pydantic import BaseModel

#date_finish = datetime.now() + timedelta(days=1) -- Para la funcion de agregar dias de vencimiento


class DocumentoInDB(BaseModel):
    id_radicado: int = 0
    username: str
    date_up: datetime = datetime.now()
    tip:str
    status: str
    # Encargado: str               Persona encargada de tramitar el documento

database_documento = []
generator = {"id":0}

database_documento = {
    "1": DocumentoInDB(**{"id_radicado":"1",
                          "username":"Amir",
                          "date_up":"2020-12-09",
                          "tip":"derecho de peticion"
                          "status":"por asignacion"}),

    "2": DocumentoInDB(**{"id_radicado":"2",
                          "username":"Juan",
                          "date_up":"2020-12-08",
                          "tip":"tutela"
                          "status":"por asignacion"}),


def save_documento(documento_in_db: DocumentoInDB):
    generator["id"] = generator["id"] + 1
    documento_in_db.id_radicado = generator["id"]
    database_documentos.append(documento_in_db)
    return documento_in_db

def consultar_documento(documento_in_db:DocumentoInDB)
    if id_radicado in database_documento:
        return database_documento[id_radicado]
    else:
        return None




