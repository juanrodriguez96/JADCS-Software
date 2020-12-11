from datetime import datetime
from pydantic import BaseModel
from typing import Dict
from db.perfil_usuario_db import persona, getUsuario

# date_finish = datetime.now() + timedelta(days=1) -- Para la funcion de agregar dias de vencimiento


class DocumentoInDB(BaseModel):
    id_radicado: str
    fecha_radicacion: datetime
    fecha_asignacion: datetime = datetime.now()
    fecha_vencimiento: datetime
    tipo: str
    status: str
    anexos: int = 0


database_documento = Dict[str, DocumentoInDB]
generator = {"id": 0}

database_documento = {
    "camilo24": [DocumentoInDB(**{
        "id_radicado": "202012001",
        "fecha_radicacion": "2020-12-09",
        "fecha_vencimiento": "2021-01-09",
        "tipo": "derecho de peticion",
        "status": "no vencido"})],

    "andres18": [DocumentoInDB(**{
        "id_radicado": "202012002",
        "fecha_radicacion": "2020-12-09",
        "fecha_vencimiento": "2020-12-30",
        "tipo": "tutela",
        "status": "no vencido",
        "anexos": 2})],
}


def mostrar_lista(id_usuario: str):
    return database_documento[id_usuario]


def agregar_doc_lista(documento_in_db: DocumentoInDB, id_usuario: str):
    if(getUsuario(id_usuario)):
        database_documento[id_usuario].append(documento_in_db)
        return database_documento


def quitar_doc_lista(radicado: str, id_usuario: str):
    return lista.remove()
  


def actualizar_documento(doc: DocumentoInDB, id_usuario: str):
    database_documento[id_usuario] = doc
    return doc
