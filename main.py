from db.resumen_estado_db import listar_documentos_usuario, definir_semaforo, agregar_doc_lista
from db.perfil_usuario_db import getUsuario
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


@app.post("/cargar/documento/")
async def agregar_doc(documento: resumen_estado_db.DocumentoInDB):
    operacion_exitosa = resumen_estado_db.agregar_doc_lista(documento)
    if operacion_exitosa:
        if (getUsuario(id_usuario)):
            definir_semaforo(documento_in_db)
            database_documento[id_usuario].append(documento_in_db)
            return database_documento 
        else: 
            raise HTTPException(status_code=400, detail="El radicado ya existe en la base de datos")  
    
     
