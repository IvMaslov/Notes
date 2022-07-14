from .base import metadata,engine
from .users import users
from .notes import notes

metadata.create_all(bind=engine)