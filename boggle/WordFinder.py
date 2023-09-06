from prefix_trie import PrefixTrie

from .Board import Board


class WordFinder:
    def __init__(self, *, board: Board = None, prefix_trie: PrefixTrie = None):
        self.board = board
        self.trie = prefix_trie

    def find_words(self) -> [str]:
        return []
