from random import choices
from typing import List


class Board:
    def __init__(self, letters: List[List[str]]):
        self.validate_letters(letters)

        self.letters = letters
        self.height = len(letters)
        self.width = len(letters[0])


    def validate_letters(self, letters):
        height = len(letters)
        assert height > 0, "Height of board must be nonzero"

        for row in letters:
            assert height == len(row), "All rows must have same length as height"

    @staticmethod
    def random(size=4):
        assert size > 0, "Size of board must be greater than 0"

        letters = []

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for i in range(size):
            letters.append(choices(alphabet, k=size))

        return Board(letters)

    def __repr__(self):
        return "\n".join("".join(row).upper() for row in self.letters)
