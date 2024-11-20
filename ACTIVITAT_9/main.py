from fastapi import FastAPI
from db_connect.connection import createConection
from crud.uses import read_users
from schemas.user_schema import users_schema

app = FastAPI()



@app.get("/users/")
async def getAllUsers():
    conn = createConection()
    users = users_schema(read_users(conn))
    conn.close()
    return users