from typing import Tuple


class Cell:
    def __init__(self, *, x: int = None, y: int = None, letter: str = None):
        self.x = x
        self.y = y
        self.letter = letter
        self.neighbors = []
        self.neighbors_set = set()

    def add_neighbor(self, neighbor: 'Cell'):
        self.neighbors.append(neighbor)
        self.neighbors_set.add(neighbor)

    def is_neighbor(self, neighbor: 'Cell'):
        return neighbor in self.neighbors_set

    def vec(self) -> Tuple[int, int]:
        return self.x, self.y

    def __hash__(self):
        return hash(self.vec())

    def __repr__(self):
        return str(str(self.vec()) + ": " + self.letter)
