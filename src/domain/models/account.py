from dataclasses import dataclass


@dataclass(frozen=True)
class Account:
    id: str
    username: str
