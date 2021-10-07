from src.domain.models.account import Account
from src.domain.repo import LoadAccountByIdRepo
from src.application.controllers.controller import Controller


class LoadAccountByIdController(Controller):
    load_account_by_id: LoadAccountByIdRepo

    def __init__(self, load_account_by_id: LoadAccountByIdRepo):
        super().__init__()
        self.load_account_by_id = load_account_by_id

    async def perform(self, request) -> Account:
        data = await self.load_account_by_id.load_by_id(request.id)
        if not data:
            return self.no_content()
        return self.ok(data)
