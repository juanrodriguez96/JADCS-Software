from typing import  Dict
from pydantic import BaseModel

class persona(BaseModel):
    idUsuario:      str # correo institucional
    contrasenia:    str
    nombre:         str
    apellido:       str
    categoria:      str



database_users = Dict[str, persona]

database_users = {
    "camilo24": persona(**{"idUsuario":"camilo24",
                            "contrasenia":"root",
                            "nombre":"camilo",
                            "apellido":"perez",
                            "categoria":"Jefe"}),

    "andres18": persona(**{"idUsuario":"andres18",
                            "contrasenia":"hola",
                            "nombre":"andres",
                            "apellido":"lopez",
                            "categoria":"No jefe"}),

    "batman": persona(**{"idUsuario":"batman",
                            "contrasenia":"batroot",
                            "nombre":"bruce",
                            "apellido":"wayne",
                            "categoria":"Jefe"}),

    "robin": persona(**{"idUsuario":"robin",
                            "contrasenia":"root",
                            "nombre":"dick",
                            "apellido":"grayson",
                            "categoria":"No jefe"}),

    "batgirl": persona(**{"idUsuario":"batgirl",
                            "contrasenia":"root",
                            "nombre":"barbara",
                            "apellido":"gordon",
                            "categoria":"No jefe"})
}

def getUsuario (user: str):

    if user in database_users.keys():
        return database_users[user]
    else:
        return None

def updateUsuario(user: persona):
    database_users[user.idUsuario] = user
    return user

def createUsuario (user: persona):
    database_users[user.idUsuario] = user
    return user
