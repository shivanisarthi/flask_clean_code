from src.domain.models.account import Account
from src.domain.repo.add_account_repo import AddAccountRepo
from src.application.protocols.controller import Controller


class AddAccountController(Controller):
    add_account_repo: AddAccountRepo

    def __init__(self, add_account_repo: AddAccountRepo):
        self.add_account_repo = add_account_repo

    async def handle(self, request: any) -> Account:
        try:
            return await self.add_account_repo.add(request)
        except Exception as e:
            print(e)
