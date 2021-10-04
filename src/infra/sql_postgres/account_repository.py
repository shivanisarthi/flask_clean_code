from src.domain.repo.add_account_repo import AddAccountRepo
from src.domain.models.account import Account
from src.infra.sql_postgres.models import AccountModel, db


class AccountRepository(AddAccountRepo):
    async def add(self, account: Account) -> Account:
        account_model = AccountModel(username=account.username)
        await account_model.create()
        print(account_model)
        return Account(id=account_model.id, username=account_model.username)
