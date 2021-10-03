from src.domain.models.account import Account
from src.domain.repo.add_account_repo import AddAccountRepo
from src.application.controllers.controller import Controller


class AddAccountController(Controller):
    add_account_repo: AddAccountRepo

    def __init__(self, add_account_repo: AddAccountRepo):
        super()
        self.add_account_repo = add_account_repo

    async def perform(self, request: Account) -> Account:
        data = await self.add_account_repo.add(request)
        return self.ok(data)

    def validation(self, request: Account) -> Exception:
        if not hasattr(request, 'id'):
            return Exception('Missing id')
        if not hasattr(request, 'name'):
            return Exception('Missing name')
