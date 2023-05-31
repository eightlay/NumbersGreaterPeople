from __future__ import annotations
from typing import Any
from copy import deepcopy
from abc import ABC, abstractmethod, abstractstaticmethod


class Storage(ABC):
    @abstractmethod
    def __init__(self) -> None:
        self.index = 0
        self.current = 0

    @abstractmethod
    def update(self, value: Any) -> bool:
        pass

    @abstractmethod
    def initial_messages(self) -> list[str]:
        pass

    @abstractstaticmethod
    def _defaults() -> Storage:
        pass

    @classmethod
    def defaults(cls) -> Storage:
        return cls._defaults().copy()

    def to_message(self) -> str:
        return f"*№{self.index}*\n\n{self.current}"

    def copy(self) -> Storage:
        return deepcopy(self)
