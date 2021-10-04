from src.application.controllers import AddAccountController
from src.infra.sql_postgres import AccountRepository
from src.infra.schema_validator import SchemaAdapter, schema_account


def makeAddAccount() -> AddAccountController:
    return AddAccountController(AccountRepository(), SchemaAdapter(schema_account))
