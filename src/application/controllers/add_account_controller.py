from src.domain.models.account import Account
from src.domain.repo import AddAccountRepo
from src.application.controllers.controller import Controller
from src.application.validator import Validator


class AddAccountController(Controller):
    add_account_repo: AddAccountRepo
    validator: Validator

    def __init__(self, add_account_repo: AddAccountRepo, validator: Validator):
        super().__init__(validator)
        self.add_account_repo = add_account_repo

    async def perform(self, request: Account) -> Account:
        data = await self.add_account_repo.add(request)
        return self.ok(data)
