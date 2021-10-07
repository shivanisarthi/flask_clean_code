from src.domain.models.account import Account
from src.domain.repo import LoadAccountById
from src.application.controllers.controller import Controller


class LoadAccountByIdController(Controller):
    load_account_by_id_repo: LoadAccountById

    def __init__(self, load_account_by_id_repo: LoadAccountById):
        super().__init__()
        self.load_account_by_id_repo = load_account_by_id_repo

    async def perform(self, request) -> Account:
        data = await self.load_account_by_id_repo.load_by_id(request.id)
        return self.ok(data)
