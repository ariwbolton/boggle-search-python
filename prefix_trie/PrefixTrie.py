from .Node import Node

class PrefixTrie:
    def __init__(self):
        self.root = Node()

    @staticmethod
    def from_words(words: [str]) -> 'PrefixTrie':
        trie = PrefixTrie()

        for word in words:
            trie.root.insert_word(word)

        return trie

    @staticmethod
    def from_file(filename: str):
        with open(filename) as f:
            lines = [line.strip().lower() for line in f.readlines()]

        return PrefixTrie.from_words(lines)