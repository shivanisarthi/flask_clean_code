from abc import ABCMeta, abstractmethod
from typing import Any


class Controller(metaclass=ABCMeta):
    @abstractmethod
    async def handle(self, request: Any) -> Any:
        raise NotImplementedError

    def no_content():
        return '', 204
