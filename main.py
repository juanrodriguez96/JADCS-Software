from db.perfil_usuario_db import Persona
from db.perfil_usuario_db import getUsuario, mostrarBase
from modelos.perfil_usuario_modelo import personaIn
from datetime import datetime
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/usuarios")
async def get_usuarios():
    labase = mostrarBase()
    return labase
