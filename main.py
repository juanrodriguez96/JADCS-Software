from db.perfil_usuario_db import Persona
from db.perfil_usuario_db import getUsuario, mostrarBase
from modelos.perfil_usuario_modelo import personaIn
from datetime import datetime
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Sistema de Gestión Documental"}


@app.post("/autenticar")
async def auth_user(user_in: personaIn):
    user_in_db = getUsuario(user_in.idUsuario)

    if user_in_db is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.contrasenia != user_in.contrasenia:
        return {"Autenticado": False}

    return {"Autenticado": True}


@app.get("/usuarios")
async def get_usuarios():
    labase = mostrarBase()
    return labase

@app.delete("usuario/documento/borrar")
async def eliminar_documento():
    lista = database_documento(idUsuario)
    if idUsuario is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    else:
        for i in range(len(lista)):
            if lista[i].id_radicado == radicado:
                del database_documento(id_usuario)[i]
                return quitar_doc_lista()


