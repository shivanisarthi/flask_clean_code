
from src.domain.repo.add_account_repo import AddAccountRepo
from src.domain.models.account import Account


class AccountRepository(AddAccountRepo):

    async def add(self, account: Account) -> Account:
        return Account(account.id, account.name)
