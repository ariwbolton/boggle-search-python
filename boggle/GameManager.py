from prefix_trie import PrefixTrie
from .Board import Board
from .WordFinder import WordFinder
from timeit import default_timer as timer


class GameManager:
    def __init__(self):
        self.timings = {}

    def run(self):
        dictionary = self.load_dictionary()

        board = self.create_board()

        words = self.find_words(board, dictionary)

        self.report_words(words)

    def load_dictionary(self):
        print("Loading dictionary... ", end="")
        start = timer()

        dictionary = PrefixTrie.from_file("words")

        end = timer()
        print("Done")

        self.timings["load_dictionary"] = end - start

        return dictionary

    def create_board(self):
        print("\nBoard\n---")
        board = Board.from_dice()
        print(board)

        return board

    def find_words(self, board, dictionary):
        print("\nFinding words... ", end="")
        word_finder = WordFinder(board=board, prefix_trie=dictionary)

        words = word_finder.find_words()

        print("Done")

        return words

    def report_words(self, words):
        sorted_words = list(sorted(words, key=lambda word: -len(word)))
        scorable_words = [word for word in sorted_words if len(word) >= 3]
        long_words = [word for word in sorted_words if len(word) >= 5]
        long_words_str = "\n".join(long_words)
        points = sum(self.score_word(word) for word in words)

        print("\nResults\n---")
        print(f"Long words (5+):\n{long_words_str}\n")
        print(f"# Words (3+): {len(scorable_words)}")
        print(f"Points: {points}")
        print(f"Timings: {self.timings}")

    def score_word(self, word: str):
        length = len(word)

        if length <= 2:
            return 0
        if length == 3 or length == 4:
            return 1
        if length == 5:
            return 2
        if length == 6:
            return 3
        if length == 7:
            return 5
        if length >= 8:
            return 11