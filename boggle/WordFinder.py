from typing import Set

from prefix_trie import PrefixTrie, Visitor

from .Board import Board
from .Path import Path


class WordFinder:
    def __init__(self, *, board: Board = None, prefix_trie: PrefixTrie = None):
        self.board = board
        self.trie = prefix_trie

    def find_words(self) -> [str]:
        words_set = set()

        for cell in self.board.cells():
            path = Path(start=cell)
            visitor = Visitor(start=cell.letter, trie=self.trie)

            self.recurse_path(path=path, visitor=visitor, words_set=words_set)

        return list(sorted(words_set))

    def recurse_path(self, path: Path, visitor: Visitor, words_set: Set):
        if visitor.current().is_terminal:
            words_set.add(path.word())

        for neighbor in path.current().neighbors:
            if not path.seen(neighbor) and visitor.can_visit(neighbor.letter):
                path.step(neighbor)
                visitor.step(neighbor.letter)

                self.recurse_path(path=path, visitor=visitor, words_set=words_set)

                path.backtrack()
                visitor.backtrack()
