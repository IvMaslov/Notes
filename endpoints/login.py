from fastapi import APIRouter, Depends, HTTPException,status,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from repositories.users import UserRepository
from .depends import get_user_repository,get_current_user
from typing import List
from models.user import User,UserIn

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def create_user(request: Request):
	return templates.TemplateResponse("create_user.html", {"request":request})

