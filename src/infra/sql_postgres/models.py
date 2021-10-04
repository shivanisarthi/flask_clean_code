from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.infra.date.datetime import get_current_date

db = SQLAlchemy()
migrate = Migrate()


class BaseModel:
    created_at = db.Column("created_at", db.DateTime, nullable=True, default=None)
    updated_at = db.Column("updated_at", db.DateTime, nullable=True, default=None)

    def create(self):
        self.created_at = get_current_date()
        db.session.add(self)
        db.session.commit()
        return self


class AccountModel(db.Model, BaseModel):
    __tablename__ = "Account"

    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(50), nullable=True)

    def __init__(self, username: str) -> None:
        super().__init__()
        self.username = username
