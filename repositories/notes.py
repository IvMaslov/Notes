
from typing import List
from db.notes import notes
import datetime
from models.notes import Notes,NotesIn,NotesStart
from models.user import User
from .base import BaseRepository

class NotesRepository(BaseRepository):

	async def create(self, u: NotesIn) -> Notes:
		note = Notes(
				user_email=u.user_email,
				title=u.title,
				text=u.text,
				created_date=datetime.datetime.utcnow(),
				updated_date=datetime.datetime.utcnow()
		)
		values = {**note.dict()}
		values.pop("id",None)
		query = notes.insert().values(**values)
		note.id = await self.database.execute(query=query)
		return note


	async def update(self, id: int, u: NotesIn) -> Notes:
		note = Notes(
				id=id,
				user_email=u.user_email,
				title=u.title,
				text=u.text,
				created_date=datetime.datetime.utcnow(),
				updated_date=datetime.datetime.utcnow()
		)
		values = {**note.dict()}
		values.pop("id",None)
		values.pop("created_date",None)
		query = notes.update().where(notes.c.id==id).values(**values)
		await self.database.execute(query=query)
		return note


	async def delete(self,id: int) -> int:
		query = notes.delete().where(notes.c.id==id)
		return await self.database.execute(query=query)


	async def get_all(self, email: str) -> List[Notes]:
		query = notes.select().where(notes.c.user_email==email)
		return await self.database.fetch_all(query=query)


	async def get_by_id(self, id: int, email: str) -> Notes:
		query = notes.select().filter(notes.c.id == id,notes.c.user_email==email)
		note = await self.database.fetch_one(query=query)
		if not note:
			return None
		return Notes.parse_obj(note)

