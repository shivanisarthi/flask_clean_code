from src.application.controllers import AddAccountController
from src.infra.schema_validator import schema_account, SchemaAdapter
from src.main.factories import make_repo_account


def make_add_account() -> AddAccountController:
    return AddAccountController(make_repo_account(), SchemaAdapter(schema_account))
