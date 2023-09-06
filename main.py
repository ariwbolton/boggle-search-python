"""
# boggle-search-python

Includes generating boards, loading existing boards, and searching for words
"""

from boggle import Board

def run():
    board = Board.random(size=4)

    print(board)



if __name__ == '__main__':
    run()