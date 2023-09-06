from typing import Dict


class Node:
    def __init__(self):
        self.children: Dict[str, Node] = {}
        self.is_terminal = False


    def insert_word(self, word):
        assert len(word) != 0

        if len(word) == 1:
            self.is_terminal = True
        else:
            # TODO: use setdefault?
            if self.has_child(word):
                self.create_child(word)

            self.get_child(word).insert_word(word[1:])

    def is_word(self, word):
        assert len(word) != 0

        if len(word) == 1 and self.is_terminal:
            return True
        elif self.has_child(word):
            return self.get_child(word).is_word(word[1:])
        else:
            # Not a terminal and no child means this isn't a word
            return False

    def has_child(self, word):
        return word[0] in self.children

    def get_child(self, word):
        return self.children[word[0]]

    def create_child(self, word):
        self.children[word[0]] = Node()

