from db.resumen_estado_db import listar_documentos_usuario, definir_semaforo
from db.perfil_usuario_db import getUsuario
from db.perfil_usuario_db import persona
from db.perfil_usuario_db import getUsuario, updateUsuario, createUsuario
from db.supervision_db import Supervision
from db.supervision_db import getSupervision, updateSupervision
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

@app.get("/usuario/perfil/{usuario}")
async def get_Equipo(usuario: str):
    user = getUsuario(usuario)
    if user == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    equipo = getSupervision(usuario)
    if len(equipo) == 0:
        return {"Perfil" : {"Usuario": user.idUsuario,
                        "Nombre" :user.nombre,
                        "Apellido" : user.apellido,
                        "Categoria" : user.categoria,
                        "Equipo" : "Nadie a cargo"}}

    return {"Perfil" : {"Usuario": user.idUsuario,
                        "Nombre" :user.nombre,
                        "Apellido" : user.apellido,
                        "Categoria" : user.categoria,
                        "Equipo" : equipo}}
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
