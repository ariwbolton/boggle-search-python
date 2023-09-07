import string
from copy import copy
from random import choices, shuffle, choice
from typing import List
import itertools

from .CellsBuilder import CellsBuilder


# Dice! https://boardgamegeek.com/thread/300565/review-boggle-veteran-and-beware-different-version
# There's a "new" and "old" version; "new" version is apparently a bit easier

new_standard_dice = [
    "AAEEGN",
    "ELRTTY",
    "AOOTTW",
    "ABBJOO",
    "EHRTVW",
    "CIMOTU",
    "DISTTY",
    "EIOSST",
    "DELRVY",
    "ACHOPS",
    "HIMNQU",
    "EEINSU",
    "EEGHNW",
    "AFFKPS",
    "HLNNRZ",
    "DEILRX"
]

old_standard_dice = [
    "AACIOT",
    "AHMORS",
    "EGKLUY",
    "ABILTY",
    "ACDEMP",
    "EGINTV",
    "GILRUW",
    "ELPSTU",
    "DENOSW",
    "ACELRS",
    "ABJMOQ",
    "EEFHIY",
    "EHINPS",
    "DKNOTU",
    "ADENVZ",
    "BIFORX"
]

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


class Board:
    def __init__(self, letters: List[List[str]]):
        self.cell_grid = CellsBuilder().build_cells(letters)
        self.height = len(self.cell_grid)
        self.width = len(self.cell_grid[0])

    def cells(self):
        return itertools.chain(*self.cell_grid)

    @staticmethod
    def random(*, size=4):
        assert size > 0, "Size of board must be greater than 0"

        letters = []

        for i in range(size):
            letters.append(choices(string.ascii_lowercase, k=size))

        return Board(letters)

    @staticmethod
    def from_dice(*, version="new"):
        dice = new_standard_dice if version == "new" else old_standard_dice
        dice = copy(dice)  # some methods will mutate this list

        shuffle(dice)

        size = 4  # hardcoded because only available dice versions are for 4x4 games
        dice_grid = grouper(dice, size)

        letters = []

        for row in dice_grid:
            letters.append([choice(die).lower() for die in row])

        return Board(letters)


    def __repr__(self):
        return "\n".join("".join(cell.letter for cell in row).upper() for row in self.cell_grid)
