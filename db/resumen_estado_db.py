from datetime import date
from pydantic import BaseModel
from typing import Dict
from db.perfil_usuario_db import persona, getUsuario

# date_finish = datetime.now() + timedelta(days=1) -- Para la funcion de agregar dias de vencimiento


class DocumentoInDB(BaseModel):
    id_radicado: str
    fecha_radicacion: date
    fecha_asignacion: date = date.today()
    fecha_vencimiento: date
    tipo: str
    status: str
    anexos: int = 0
    # Derecho de petición = 15(5,10,15) Tutelas = 5(5) Consultas = 25(5,15,25)
    tipo: str
    status: str
    anexos: int = 0
    semaforo: str


database_documento = Dict[str, DocumentoInDB]
generator = {"id": 0}

database_documento = {
    "camilo24": [DocumentoInDB(**{
        "id_radicado": "202012001",
        "fecha_radicacion": date(2020, 12, 9),
        "fecha_vencimiento": date(2021, 1, 9),
        "tipo": "derecho de peticion",
        "status": "no vencido",
        "semaforo": "verde"})],

    "andres18": [DocumentoInDB(**{
        "id_radicado": "202012002",
        "fecha_radicacion": date(2020, 12, 10),
        "fecha_vencimiento": date(2021, 12, 15),
        "tipo": "tutela",
        "status": "no vencido",
        "anexos": 2,
        "semaforo": "rojo"})],
}


def definir_semaforo(documento_in_db: DocumentoInDB):
    d1 = date.today()
    d2 = documento_in_db.fecha_vencimiento
    diferencia = (d2 - d1).days
    # Derecho de petición = 15(5,10,15) Tutelas = 5(5) Consultas = 25(5,15,25)
    if(documento_in_db.tipo == "derecho de peticion"):
        if(diferencia < 6):
            documento_in_db.semaforo = "rojo"
        elif (diferencia < 11):
            documento_in_db.semaforo = "amarillo"
        else:
            documento_in_db.semaforo = "verde"
    elif(documento_in_db.tipo == "consultas"):
        if(diferencia < 6):
            documento_in_db.semaforo = "rojo"
        elif (diferencia < 15):
            documento_in_db.semaforo = "amarillo"
        else:
            documento_in_db.semaforo = "verde"
    elif(documento_in_db.tipo == "tutelas"):
        documento_in_db.semaforo = "rojo"


def listar_documentos_usuario(id_usuario: str):
    return database_documento[id_usuario]


def agregar_doc_lista(documento_in_db: DocumentoInDB, id_usuario: str):
    if(getUsuario(id_usuario)):
        # Creo que esto (el semaforo) se puede incluir en el endpoint(main) y no en este método
        definir_semaforo(documento_in_db)
        database_documento[id_usuario].append(documento_in_db)
        return database_documento


def quitar_doc_lista(radicado: str, id_usuario: str):
    lista = database_documento(id_usuario)
    for i in range(len(lista)):
        if lista[i].id_radicado == radicado:
            del database_documento(id_usuario)[i]
            return database_documento
    return None


def actualizar_documento(doc: DocumentoInDB, id_usuario: str):
    database_documento[id_usuario] = doc
    return doc
