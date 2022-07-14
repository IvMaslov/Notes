from fastapi import APIRouter,Depends,HTTPException,status,Request
from fastapi.responses import HTMLResponse
from models.token import Token,Login
from repositories.users import UserRepository
from .depends import get_user_repository
from core.security import verify_password,create_access_token
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.post("/",response_model=Token)
async def login(login: Login,user: UserRepository = Depends(get_user_repository)):
	user = await user.get_by_email(login.email)
	if user is None or not verify_password(login.password,user.hashed_password):
		raise HTTPException(status.HTTP_401_UNAUTHORIZED,detail="incorrect email or password")



	return Token(access_token=create_access_token({"sub": user.email}),
		token_type="Bearer")		


@router.get("/", response_class=HTMLResponse)
async def read_login(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})
