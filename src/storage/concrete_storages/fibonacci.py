from __future__ import annotations
from typing import Any

from storage.storage import Storage


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
            (
                "Последовательность Фибоначчи формируется следующим образом:\n\n"
                "1. Первые два числа равны 0 и 1\n"
                "2. Каждое последующее число равно сумме двух предыдущих\n\n"
                "Например:\n"
                "0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ..."
            ),
            "*№1*\n\n0",
            "*№2*\n\n1",
        ]
