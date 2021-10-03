from src.domain.repo.add_account_repo import AddAccountRepo
from src.domain.models.account import Account
from src.infra.sql_postgres.models import AccountModel, db


class AccountRepository(AddAccountRepo):

    async def add(self, account: Account) -> Account:
        account = AccountModel(username=account.username)
        db.session.add(account)
        db.session.commit()
        return Account(id=account.id, username=account.username)
