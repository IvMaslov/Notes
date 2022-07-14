import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, validator, constr

class Notes(BaseModel):
	id: Optional[int] = None
	user_email: EmailStr
	title: str
	text: str
	created_date: datetime.datetime
	updated_date: datetime.datetime


class NotesIn(BaseModel):
	user_email: EmailStr
	title: str
	text: str


class NotesStart(BaseModel):
	user_email: EmailStr