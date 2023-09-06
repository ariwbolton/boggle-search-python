from random import choices
from typing import List
import itertools

from .CellsBuilder import CellsBuilder


class Board:
    def __init__(self, letters: List[List[str]]):
        self.cell_grid = CellsBuilder().build_cells(letters)
        self.height = len(self.cell_grid)
        self.width = len(self.cell_grid[0])

    def cells(self):
        return itertools.chain(*self.cell_grid)

    @staticmethod
    def random(size=4):
        assert size > 0, "Size of board must be greater than 0"

        letters = []

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for i in range(size):
            letters.append(choices(alphabet, k=size))

        return Board(letters)

    def __repr__(self):
        return "\n".join("".join(cell.letter for cell in row).upper() for row in self.cell_grid)
