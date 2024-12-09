from typing import List

from fastapi import FastAPI
from insertDATA import connection
from schemes import schemes
from CRUD import reads, updates

app = FastAPI()
conn = connection.createConection()

@app.get("/intents", response_model=List[dict])
async def obtenirIntents(id_jugador : int):
    intents = reads.llegirNombreIntentsPartida(conn, id_jugador)
    return schemes.dadesPartida_schema(intents)

@app.post("/augmentarIntents")
async def incrementarIntents(id_jugador : int):
    updates.incrementarIntents(conn, id_jugador)
    intents = await obtenirIntents(id_jugador) #Utilitzem await perque es una funcio asincrona
    return intents

@app.get("/alfabet", response_model=dict)
async def obtenirAlfabet(idioma: str):
    alfabet = reads.llegirAlfabet(conn, idioma)
    return schemes.alfabet_schema(alfabet)

@app.get("/infoInicial", response_model=List[dict])
async def obtenirInfoInicialPartida(idioma: str):
    dadesInici = reads.llegirTextEstadistiques(conn, idioma)
    return schemes.estadistiquesTxt_schema(dadesInici)

@app.get("/puntuacioJugador", response_model=List[dict])
async def obtenirPuntuacioJugador(id_jugador: int):
    estadistiques = reads.llegirEstadistiquesJugador(conn, id_jugador)
    return schemes.estadistiques_schema(estadistiques)