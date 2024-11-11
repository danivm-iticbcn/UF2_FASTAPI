from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"bienvenida":"Bienvenido al inicio de esta API"}


class Alumno(BaseModel):
    nombre : str
    edad : int
    localidad : str | None = None


@app.post("/alumno")
async def inrtoducirAlumno(alumno: Alumno):
    return {"Alumno": alumno}