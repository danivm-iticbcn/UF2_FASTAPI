from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from insertDATA import connection
from schemes import schemes
from CRUD import reads, updates, creates, deletes

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


### ACTIVITAT 12 ###

## JUGADOR ##

class Jugador(BaseModel):
    id: int
    username: str
    password: str
    partidesJugades: int
    partidesGuanyades: int
    dataMillorPuntuacio: str
    millorPuntuacio: int

@app.put("/modificarJugador", response_model=dict)
async def modificarJugador(jugador: Jugador):
    estat = updates.modificarJugador(conn, jugador)
    return {"estat":estat}

@app.post("/insertarJugador", response_model=dict)
async def insertarJugador(jugador: Jugador):
    estat = creates.insertarJugador(conn, jugador)
    return {"estat":estat}

@app.delete("/eliminarJugador", response_model=dict)
async def eliminarJugador(idJugador: int):
    estat = deletes.eliminarJugador(conn, idJugador)
    return {"estat": estat}

@app.get("/jugador", response_model=List[dict])
async def llegirJugador():
    jugadors = reads.llegirJugador(conn)
    return schemes.jugadors_schema(jugadors)

## PARTIDA ##

class Partida(BaseModel):
    id: int
    punts: int
    estatPartida: bool
    paraula: str
    estatParaula: str
    intents: int
    jugadorId: int

@app.post("/insertarPartida", response_model=dict)
async def insertarPartida(partida: Partida):
    estat = creates.insertarPartida(conn, partida)
    return {"estat":estat}

@app.delete("/eliminarPartida", response_model=dict)
async def eliminarPartida(idPartida: int):
    estat = deletes.eliminarPartida(conn, idPartida)
    return {"estat": estat}

@app.get("/partida", response_model=List[dict])
async def llegirPartida():
    partides = reads.llegirPartida(conn)
    return schemes.partides_schema(partides)

## INICI PANTALLA ##

class IniciPantalla(BaseModel):
    idioma: str
    lletres: str
    textIniciar: str
    textPunts: str
    textTotal: str
    textGuanyades: str
    textMillorPuntuacio: str

@app.put("/modificarIniciPantalla", response_model=dict)
async def modificarIniciPantalla(iniciPantalla: IniciPantalla):
    estat = updates.modificarIniciPantalla(conn, iniciPantalla)
    return {"estat":estat}

@app.post("/insertarIniciPantalla", response_model=dict)
async def insertarIniciPantalla(iniciPantalla: IniciPantalla):
    estat = creates.insertarIniciPantalla(conn, iniciPantalla)
    return {"estat":estat}

@app.delete("/eliminarIniciPantalla", response_model=dict)
async def eliminarPartida(idioma: str):
    estat = deletes.eliminarIniciPantalla(conn, idioma)
    return {"estat": estat}


## PARAULES ##

class Paraula(BaseModel):
    paraula: str
    tematica: str

@app.put("/modificarParaula", response_model=dict)
async def modificarParaula(paraulaAntiga: Paraula, paraulaAct: Paraula):
    estat = updates.modificarParaula(conn, paraulaAntiga, paraulaAct)
    return {"estat":estat}

@app.post("/insertarParaula", response_model=dict)
async def insertarParaula(paraula: Paraula):
    estat = creates.insertarParaula(conn, paraula)
    return {"estat":estat}

@app.delete("/eliminarParaula", response_model=dict)
async def eliminarPartida(paraula: Paraula):
    estat = deletes.eliminarParaula(conn, paraula)
    return {"estat": estat}

@app.get("/paraula", response_model=List[dict])
async def llegirParaula():
    paraules = reads.llegirParaula(conn)
    return schemes.paraules_schema(paraules)