import pickle

from .Node import Node
from .WordContainer import WordContainer

class PrefixTrie:
    def __init__(self):
        self.root = Node()

    @staticmethod
    def from_words(words: [str]) -> 'PrefixTrie':
        trie = PrefixTrie()

        for word in words:
            trie.root.insert_word(WordContainer(word))

        return trie

    @staticmethod
    def from_file(filename: str):
        with open(filename) as f:
            lines = [line.strip().lower() for line in f.readlines()]

        return PrefixTrie.from_words(lines)

    @staticmethod
    def from_pkl_file(filename: str):
        with open(filename, 'rb') as f:
            trie = pickle.load(f)

        return trie

    def to_pkl_file(self, filename: str):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    def is_word(self, word: str):
        return self.root.is_word(word.lower())

    def is_prefix(self, word: str):
        return self.root.is_prefix(word.lower())

if __name__ == "__main__":
    print('loading dictionary!')
    dictionary = PrefixTrie.from_file("words")

    print('loaded dictionary!')

    print('is_word tests')

    print(dictionary.is_word("aardvark"))
    print(dictionary.is_word("nothing"))
    print(dictionary.is_word("jsdlfjslkdjls"))
    print(dictionary.is_word("Abencerrages"))

    print('is_prefix tests')

    print(dictionary.is_prefix("A"))
    print(dictionary.is_prefix("Z"))
    print(dictionary.is_prefix("Abelian"))
    print(dictionary.is_prefix("Abel"))
    print(dictionary.is_prefix("nonsensenotaword"))