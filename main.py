from db.resumen_estado_db import listar_documentos_usuario, definir_semaforo
from db.perfil_usuario_db import getUsuario
from modelos.perfil_usuario_db import personaIn, personaOut
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/resumen/{nombre}")
async def lista_doc_usuario(nombre: str):
    el_usuario = getUsuario(nombre)

    if el_usuario is None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")

    lista_doc = listar_documentos_usuario(nombre)
    if lista_doc is None:
        return {nombre: "No tiene documentos asignados"}

    for documento in lista_doc:
        definir_semaforo(documento)
    return lista_doc

#Operación POST (CREATE) para perfil de usuario
@api.post("/usuario/perfil/")
async def crear_perfil_usuario(usuario: personaIn):

    usuario_db = getUsuario(usuario.idUsuario)

    if usuario_db == None:
        createUsuario(usuario)
    elif usuario_db != None:
        return {usuario.idUsuario,"Ya existe"}

    usuario_out = personaOut(**usuario_db.dict())
    return usuario_out
