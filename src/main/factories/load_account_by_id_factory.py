from src.application.controllers import LoadAccountByIdController
from src.main.factories import make_repo_account


def make_load_account_by_id() -> LoadAccountByIdController:
    return LoadAccountByIdController(make_repo_account())
