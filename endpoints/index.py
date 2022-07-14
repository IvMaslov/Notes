from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/")
def read_index():

	return RedirectResponse("/auth/")