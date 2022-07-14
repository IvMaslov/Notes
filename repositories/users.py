import datetime
from typing import List, Optional
from db.users import users
from core.security import hashed_password
from models.user import UserIn, User
from .base import BaseRepository

class UserRepository(BaseRepository):

	async def create(self,u: UserIn) -> User:
		user = User(
            name=u.name,
            email=u.email,
            hashed_password=hashed_password(u.password),
            created_date=datetime.datetime.utcnow(),
            updated_date=datetime.datetime.utcnow(),
        )
		values = {**user.dict()}
		values.pop("id", None)
		query = users.insert().values(**values)
		user.id = await self.database.execute(query)
		return user


	async def update(self, id: int,u: UserIn) -> User:
		user = User(
			id=id,
			name=u.name,
			email=u.email,
			hashed_password=hashed_password(u.password2),
			created_date=datetime.datetime.utcnow(),
			updated_date=datetime.datetime.utcnow()
			)
		values = {**user.dict()}
		values.pop("id", None)
		values.pop("created_date", None)
		query = users.update().where(users.c.id==id).values(**values)
		await self.database.execute(query=query)
		return user


	async def delete(self,id: int):
		query = users.delete().where(users.c.id==id)
		return await self.database.execute(query=query)


	async def get_all(self,limit: int=100,skip: int=0) -> List[User]:
		query = users.select().limit(limit).offset(skip)
		return await self.database.fetch_all(query=query)


	async def get_by_id(self, id: int) -> Optional[User]:
		query = users.select().where(users.c.id==id)
		user = await self.database.fetch_one(query)
		if user is None:
			return None
		return User.parse_obj(user)


	async def get_by_email(self, email: str) -> User:
		query = users.select().where(users.c.email==email)
		user = await self.database.fetch_one(query)
		if user is None:
			return None
		return User.parse_obj(user)