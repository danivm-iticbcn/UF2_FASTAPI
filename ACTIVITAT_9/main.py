from fastapi import FastAPI
import connection
import uses
import schema

app = FastAPI()



@app.get("/users/")
async def getAllUsers():
    return schema.users_schema(uses.read_users(connection.createConection()))