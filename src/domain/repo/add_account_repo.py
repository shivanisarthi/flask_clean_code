from abc import ABCMeta, abstractmethod

from src.domain.models.account import Account


class AddAccountRepo(metaclass=ABCMeta):
    @abstractmethod
    async def add(self, account: Account) -> Account:
        raise NotImplementedError
