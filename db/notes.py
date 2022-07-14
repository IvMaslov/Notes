from .base import metadata
import datetime
import sqlalchemy

notes = sqlalchemy.Table(
	"notes",
	metadata,
	sqlalchemy.Column("id",sqlalchemy.Integer,primary_key=True,autoincrement=True,unique=True),
	sqlalchemy.Column("user_email",sqlalchemy.String,sqlalchemy.ForeignKey("users.email"),nullable=False),
	sqlalchemy.Column("title",sqlalchemy.String),
	sqlalchemy.Column("text",sqlalchemy.Text),
	sqlalchemy.Column("created_date",sqlalchemy.DateTime),
	sqlalchemy.Column("updated_date",sqlalchemy.DateTime)
	)