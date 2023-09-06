from random import choices
from typing import List

from .CellsBuilder import CellsBuilder


class Board:
    def __init__(self, letters: List[List[str]]):
        self.cells = CellsBuilder().build_cells(letters)
        self.height = len(self.cells)
        self.width = len(self.cells[0])

    @staticmethod
    def random(size=4):
        assert size > 0, "Size of board must be greater than 0"

        letters = []

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for i in range(size):
            letters.append(choices(alphabet, k=size))

        return Board(letters)

    def __repr__(self):
        return "\n".join("".join(cell.letter for cell in row).upper() for row in self.cells)
