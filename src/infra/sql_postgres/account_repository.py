from src.domain.repo import AddAccountRepo, LoadAccountByIdRepo
from src.domain.models import Account
from src.infra.sql_postgres import AccountModel


class AccountRepository(AddAccountRepo, LoadAccountByIdRepo):
    async def add(self, account: Account) -> Account:
        account_model = AccountModel(username=account.username).create()
        return self.__adapt_account(account_model)

    async def load_by_id(self, id: int) -> Account:
        account_model = AccountModel.query.get(id)
        return self.__adapt_account(account_model)

    def __adapt_account(self, model: AccountModel) -> Account:
        return Account(id=model.id, username=model.username) if model else None
