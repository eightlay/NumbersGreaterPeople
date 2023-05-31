from __future__ import annotations
from typing import Any

from storage.storage import Storage


class EvensStorage(Storage):
    def __init__(self, current: int, index: int) -> bool:
        self.index = index
        self.current = current
        self.next = current + 2

    def update(self, value: Any) -> None:
        try:
            value = int(value)
        except ValueError:
            return False

        if value != self.next:
            return False

        self.index += 1
        self.current, self.next = self.next, self.next + 2

        return True

    @staticmethod
    def _defaults() -> EvensStorage:
        return EvensStorage(2, 1)

    def initial_messages(self) -> list[str]:
        return [
            (
                "Число называется чётным, если оно делится на 2 без остатка.\n"
                "Например:\n"
                "2, 4, 6, 8, 10, 12, 14, 16, 18, 20, ..."
            ),
            "*№1*\n\n2",
        ]
