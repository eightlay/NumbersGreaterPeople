class Topic:
    def __init__(self, name: str, id: int) -> None:
        self.name = name
        self.id = id

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, Topic):
            return self.id == other.id
        if isinstance(other, int):
            return self.id == other
        return False
