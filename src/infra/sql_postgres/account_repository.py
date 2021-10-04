from src.domain.repo import AddAccountRepo
from src.domain.models import Account
from src.infra.sql_postgres import AccountModel


class AccountRepository(AddAccountRepo):
    async def add(self, account: Account) -> Account:
        account_model = AccountModel(username=account.username).create()
        return Account(id=account_model.id, username=account_model.username)
