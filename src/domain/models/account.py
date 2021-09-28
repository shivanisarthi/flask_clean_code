from dataclasses import dataclass


@dataclass(frozen=True)
class Account:
    id: str
    name: str
