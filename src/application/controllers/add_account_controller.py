from types import SimpleNamespace
from src.domain.models.account import Account
from src.domain.repo.add_account_repo import AddAccountRepo
from src.application.protocols.controller import Controller


class AddAccountController(Controller):
    add_account_repo: AddAccountRepo

    def __init__(self, add_account_repo: AddAccountRepo):
        self.add_account_repo = add_account_repo

    async def handle(self, request: Account) -> Account:
        try:
            error = self.validation(request)
            if error:
                return self.bad_request(error)
            data = await self.add_account_repo.add(request)
            return self.ok(data)
        except Exception as e:
            return self.server_error(e)

    def validation(self, request: SimpleNamespace) -> Exception:
        if not hasattr(request, 'id'):
            return Exception('Missing id')
        if not hasattr(request, 'name'):
            return Exception('Missing name')
