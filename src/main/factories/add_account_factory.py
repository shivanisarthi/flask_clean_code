from src.application.controllers import AddAccountController
from src.infra.sql_postgres import AccountRepository


def makeAddAccount() -> AddAccountController:
    return AddAccountController(add_account_repo=AccountRepository())
