import random
from typing import List
from fastapi import FastAPI

from CRUD import uses
from schemes import paraules_schema, themes_schema
from insertDATA.connection import createConection

app = FastAPI()
conn = createConection()

@app.get("/penjat/tematica/opcions", response_model=List[dict])
async def getAllOptions():
    temes = uses.read_themes(conn)
    return themes_schema.themes_schema(temes)


@app.get("/penjat/tematica/{option}", response_model=List[dict])
async def getOneRandomWord(option: str):
    paraules = uses.read_word(conn, option.upper())
    paraulaFinal = paraules[random.randint(0,len(paraules)-1)]
    return paraules_schema.paraules_schema(paraulaFinal)
