from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/", status_code=404) #Status_code para cambiar el codigo que devolvemos
async def root():
    return {"bienvenida":"Bienvenido al inicio de esta API"}

#BaseModel para el post
class Alumno(BaseModel):
    nombre : str
    id : int
    edad : int
    localidad : str | None = None   #Campo opcional
    estudios : str
    curso : str

#Post
@app.post("/alumno")
async def inrtoducirAlumno(alumno: Alumno):
    return {"Alumno": alumno}