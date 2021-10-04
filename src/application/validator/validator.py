from abc import ABCMeta, abstractmethod
from typing import Any


class Validator(metaclass=ABCMeta):
    @abstractmethod
    def validate(self, data: Any) -> Exception:
        raise NotImplementedError
