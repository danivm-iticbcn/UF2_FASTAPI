from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"bienvenida":"Bienvenido al inicio de esta API"}
