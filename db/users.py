from .base import metadata
import datetime
import sqlalchemy

users = sqlalchemy.Table(
	"users",
	metadata,
	sqlalchemy.Column("id",sqlalchemy.Integer,primary_key=True,autoincrement=True,unique=True),
	sqlalchemy.Column("email",sqlalchemy.String,primary_key=True,unique=True),
	sqlalchemy.Column("name",sqlalchemy.String),
	sqlalchemy.Column("hashed_password",sqlalchemy.String),
	sqlalchemy.Column("created_date",sqlalchemy.DateTime,default=datetime.datetime.utcnow),
	sqlalchemy.Column("updated_date",sqlalchemy.DateTime,default=datetime.datetime.utcnow),

)