from starlette.config import Config
config = Config(".env")

DATABASE_URL = "postgresql://root:root@localhost:32700/notes"
ACCESS_TOKEN_EXPIRE_MINUTE = 60
ALGORITHM = "HS256"
SECRET_KEY = config("EE_SECRET_KEY",cast=str,default="74bc78d9d1b5081367362d1ed60476caa819537c6f405880c327884a3106a214")