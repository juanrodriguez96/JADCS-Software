from fastapi import FastAPI, HTTPException
from modelos.resumen_estado_doc_modelo import DocumentoIn
from modelos.perfil_usuario_modelo import personaIn, personaOut
from db.resumen_estado_db import DocumentoInDB 
from db.resumen_estado_db import listar_documentos_usuario, definir_semaforo, agregar_doc_lista, quitar_doc_lista
from db.perfil_usuario_db import getUsuario
from db.perfil_usuario_db import persona
from db.perfil_usuario_db import getUsuario, updateUsuario, createUsuario
from db.supervision_db import Supervision
from db.supervision_db import getSupervision, updateSupervision

app = FastAPI()


@app.get("/resumendoc/{nombre}")
async def lista_doc_usuario(nombre: str):
    el_usuario = getUsuario(nombre)
    if el_usuario is None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existeee")

    lista_doc = listar_documentos_usuario(nombre)
    if lista_doc is None:
        return {nombre: "No tiene documentos asignados"}

    for documento in lista_doc:
        definir_semaforo(documento)
    return lista_doc


@app.post("/cargar/documento")
async def agregar_doc(documento: DocumentoIn, nombre: str):
    if getUsuario(nombre) is None:
        raise HTTPException(status_code=404, detail="El usuario no existee")

    documento_db = DocumentoInDB(**documento.dict(), semaforo="")
    definir_semaforo(documento_db)
    operacion_exitosa = agregar_doc_lista(documento_db, nombre)

    if operacion_exitosa is None:
        return {documento.id_radicado: "Ya estaba asignado a " + nombre}

    return operacion_exitosa

@app.delete("/usuario/documento/borrar")
async def eliminar_documento(nombre: str, id_radicado: str):
    if getUsuario(nombre) is None:
        raise HTTPException(status_code=404, detail="El usuario no existee")
    if (quitar_doc_lista(nombre, id_radicado) == False):
        return {"mensaje":"Este radicado no esta asignado a este persona"}
    else:
        return {"mensaje":"Se a eliminado correctamente el radicado"}


# Operación GET (READ) para perfil de usuario

@app.get("/usuario/perfil/{usuario}")
async def get_Equipo(usuario: str):
    user = getUsuario(usuario)
    if user == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    # Mostrar si el usuario tiene un equipo a cargo
    equipo = getSupervision(usuario)
    if len(equipo) == 0:
        return {"Perfil": {"Usuario": user.idUsuario,
                           "Nombre": user.nombre,
                           "Apellido": user.apellido,
                           "Categoria": user.categoria,
                           "Equipo": "Nadie a cargo"}}

    return {"Perfil": {"Usuario": user.idUsuario,
                       "Nombre": user.nombre,
                       "Apellido": user.apellido,
                       "Categoria": user.categoria,
                       "Equipo": equipo}}


@app.post("/usuario/perfil/")
async def crear_perfil_usuario(usuario: persona):
    usuario_in_db = getUsuario(usuario.idUsuario)
    if usuario_in_db is None:
        createUsuario(usuario)
    else:
        return {usuario.idUsuario: "Ya existe"}

    usuario_out = personaOut(**usuario.dict())
    return usuario_out


@app.put("/usuario/perfil/")
async def modificar_perfil_usuario(usuario: persona):

    usuario_db = getUsuario(usuario.idUsuario)
    if usuario_db is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if usuario_db.contrasenia != usuario.contrasenia:
        return {"Autenticado": False}

    usuario_db.nombre = usuario.nombre
    usuario_db.apellido = usuario.apellido
    usuario_db.categoria = usuario.categoria

    updateUsuario(usuario_db)
    return {usuario.idUsuario: "Modificado correctamente"}
