from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class AccountModel(db.Model):
    __tablename__ = 'Account'

    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(50), nullable=True)

    def __init__(self, username: str) -> None:
        super().__init__()
        self.username = username
