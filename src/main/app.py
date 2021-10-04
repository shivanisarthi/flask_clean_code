from flask import Flask
from src.main.routes.account_routes import set_account_routes
from src.main.config.base import config_by_name
from src.infra.sql_postgres import db, migrate


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name["dev"])
    app = set_account_routes(app)
    db.init_app(app)
    migrate.init_app(app=app, db=db)
    return app
