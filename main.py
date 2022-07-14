from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from db.base import database
from endpoints import users,auth,notes,index,login,get_email


app = FastAPI(title="Notes")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(users.router, prefix="/users",tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(notes.router, prefix="/notes", tags=["notes"])
app.include_router(login.router, prefix="/login", tags=["login"])
app.include_router(get_email.router, prefix="/get_email", tags=["get_email"])
app.include_router(index.router, prefix="", tags=["index"])

@app.on_event("startup")
async def sturtup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    