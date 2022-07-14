from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.responses import JSONResponse
from typing import List
from models.notes import Notes,NotesIn,NotesStart
from models.user import User,UserIn
from .depends import get_notes_repository,get_current_user

router = APIRouter()


@router.post("/")
async def read_notes(
		current_user: User = Depends(get_current_user)):
	return JSONResponse({"user_email": current_user.email})