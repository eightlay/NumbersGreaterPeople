from __future__ import annotations
import sympy
from typing import Any
from copy import deepcopy
from abc import ABC, abstractmethod, abstractstaticmethod

from topic import Topic


class Storage(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def update(self, value: Any) -> bool:
        pass

    @abstractmethod
    def to_message(self) -> str:
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

    def copy(self) -> Storage:
        return deepcopy(self)


class FibonacciStorage(Storage):
    def __init__(self, prev: int, current: int, index: int) -> bool:
        self.index = index
        self.prev = prev
        self.current = current

    def update(self, value: Any) -> None:
        try:
            value = int(value)
        except ValueError:
            return False

        next_number = self.prev + self.current

        if value != next_number:
            return False

        self.index += 1
        self.prev, self.current = self.current, next_number

        return True

    @staticmethod
    def _defaults() -> FibonacciStorage:
        return FibonacciStorage(0, 1, 2)

    def to_message(self) -> str:
        return f"*№{self.index}*\n\n{self.current}"

    def initial_messages(self) -> list[str]:
        return [
            "*№1*\n\n0",
            "*№2*\n\n1",
        ]


class PrimesStorage(Storage):
    def __init__(self, current: int, index: int) -> bool:
        self.index = index
        self.current = current
        self.next = sympy.nextprime(current)

    def update(self, value: Any) -> None:
        try:
            value = int(value)
        except ValueError:
            return False

        if value != self.next:
            return False

        self.index += 1
        self.current, self.next = self.next, sympy.nextprime(self.next)

        return True

    @staticmethod
    def _defaults() -> PrimesStorage:
        return PrimesStorage(2, 1)

    def to_message(self) -> str:
        return f"*№{self.index}*\n\n{self.current}"

    def initial_messages(self) -> list[str]:
        return [
            "*№1*\n\n2",
        ]


STORAGES = {
    Topic("fibonacci", 11): FibonacciStorage,
    Topic("primes", 17): PrimesStorage,
}
