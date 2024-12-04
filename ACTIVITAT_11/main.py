from typing import List

from fastapi import FastAPI
from insertDATA import connection
from schemes import schemes
from CRUD import reads

app = FastAPI()
conn = connection.createConection()

@app.get("/comencar", response_model=List[dict])
async def obtenirComencarTxt(idioma : str):
    textInici = reads.llegirComencarText(conn, idioma)
    return schemes.txts_schema(textInici)

@app.get("/intents", response_model=List[dict])
async def obtenirIntents(id_jugador : int):
    intents = reads.llegirNombreIntentsPartida(conn, id_jugador)
    return schemes.dadesPartida_schema(intents)

@app.post("/augmentarIntents", response_model=List[dict])
async def incrementarIntents():
    return [{}]