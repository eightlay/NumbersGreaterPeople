from __future__ import annotations
import sympy
from typing import Any

from storage.storage import Storage


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
            (
                "Число называется простым, если оно делится только на себя и на 1.\n\n"
                "Например:\n"
                "2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ..."
            ),
            "*№1*\n\n2",
        ]
