from src.infra.sql_postgres import AccountRepository


def make_repo_account() -> AccountRepository:
    return AccountRepository()
