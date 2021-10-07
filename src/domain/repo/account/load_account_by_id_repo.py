from abc import ABCMeta, abstractmethod
from src.domain.models import Account


class LoadAccountById(metaclass=ABCMeta):
    @abstractmethod
    async def load_by_id(self, id: int) -> Account:
        raise NotImplementedError
