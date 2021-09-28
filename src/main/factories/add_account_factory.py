from src.application.controllers.add_account_controller import AddAccountController
from src.infra.sql_postgres.account_repository import AccountRepository


def makeAddAccount() -> AddAccountController:
    return AddAccountController(add_account_repo=AccountRepository())
