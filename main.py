"""
Includes generating boards, loading existing boards, and searching for words
"""

from boggle import Board, WordFinder
from prefix_trie import PrefixTrie


def run():
    print("Loading dictionary...")
    dictionary = PrefixTrie.from_file("words")

    board = Board.random(size=4)
    print(board)

    print("\nFinding words...")
    word_finder = WordFinder(board=board, prefix_trie=dictionary)

    words = word_finder.find_words()

    print("Finished finding words!\n")

    for word in words:
        print(word)


if __name__ == '__main__':
    run()