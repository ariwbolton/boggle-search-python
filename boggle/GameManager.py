import os
from timeit import default_timer as timer

from prefix_trie import PrefixTrie
from .Board import Board
from .WordFinder import WordFinder


class GameManager:
    def __init__(self):
        self.timings = {}

    def run(self):
        dictionary = self.get_dictionary()

        board = self.create_board()

        words = self.find_words(board, dictionary)

        self.report_words(words)

    def get_dictionary(self, *, force_rebuild=False):
        is_dictionary_ready = not force_rebuild and os.path.exists("data/dictionary.pkl")
        loading_str = "Loading dictionary" if is_dictionary_ready else "Building dictionary"

        print(f"{loading_str}...", end="")
        start = timer()

        dictionary = PrefixTrie.from_pkl_file("data/dictionary.pkl") if is_dictionary_ready else PrefixTrie.from_file("data/words")

        end = timer()
        print("Done")

        timings_key = "load_dictionary" if is_dictionary_ready else "build_dictionary"
        self.timings[timings_key] = end - start

        if not is_dictionary_ready:
            print("Saving dictionary...", end="")
            start_pkl = timer()

            dictionary.to_pkl_file("data/dictionary.pkl")

            end_pkl = timer()

            print("Done")
            self.timings["save_dictionary"] = end_pkl - start_pkl

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