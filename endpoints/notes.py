from fastapi import APIRouter, Depends, HTTPException,status,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from repositories.notes import NotesRepository
from .depends import get_notes_repository,get_current_user
from typing import List
from models.notes import Notes,NotesIn,NotesStart
from models.user import User,UserIn

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def read_login(request: Request):
    return templates.TemplateResponse("notes.html", {"request": request})


@router.post("/get_all/",response_model=List[Notes])
async def read_notes(
		notes: NotesRepository = Depends(get_notes_repository),
		current_user: User = Depends(get_current_user)):
	return await notes.get_all(email=current_user.email)


@router.put("/",response_model=Notes)
async def update_note(id: int,
		note: NotesIn,
		notes: NotesRepository = Depends(get_notes_repository),
		current_user: User = Depends(get_current_user)):
	if note.user_email != current_user.email:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
	return await notes.update(id=id, u=note)


@router.post("/",response_model=Notes)
async def post_create_note(
		note: NotesIn,
		notes: NotesRepository = Depends(get_notes_repository),
		current_user: User = Depends(get_current_user)):
	if note.user_email != current_user.email:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
	return await notes.create(u=note)


@router.delete("/")
async def delete_note(
		id: int,
		note: NotesStart,
		notes: NotesRepository = Depends(get_notes_repository),
		current_user: User = Depends(get_current_user)):
	if note.user_email != current_user.email:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
	return await notes.delete(id=id)


@router.get("/{id}", response_class=HTMLResponse)
async def read_note_id(request: Request):
	return templates.TemplateResponse("note_id.html", {"request":request})


@router.post("/{id}", response_model=Notes)
async def get_note_id(
		id: int,
		notes: NotesRepository = Depends(get_notes_repository),
		current_user: User = Depends(get_current_user)):
	response = await notes.get_by_id(id=id, email=current_user.email)
	if response:
		return response
	else:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")


@router.get("/add/", response_class=HTMLResponse)
async def get_create_note(request: Request):
	return templates.TemplateResponse("new_note.html", {"request": request})