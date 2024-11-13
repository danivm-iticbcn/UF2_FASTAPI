from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    # Excepcion para controlar la respuesta en caso de tener un 404 Not Found
    raise HTTPException(status_code=404, detail="No se han encontrado datos")

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