from src.domain.models.account import Account
from src.domain.repo.add_account_repo import AddAccountRepo
from src.application.protocols.controller import Controller


class AddAccountController(Controller):
    add_account_repo: AddAccountRepo

    def __init__(self, add_account_repo: AddAccountRepo):
        self.add_account_repo = add_account_repo

    async def handle(self, request: any) -> Account:
        try:
            data = await self.add_account_repo.add(request)
            if not data:
                return self.no_content()
            return self.ok(data)
        except Exception as e:
            print(e)
            return self.server_error(e)
