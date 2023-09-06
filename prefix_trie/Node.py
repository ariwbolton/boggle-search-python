from typing import Dict


class Node:
    def __init__(self):
        self.children: Dict[str, Node] = {}
        self.is_terminal = False


    def insert_word(self, word):
        if len(word) == 0:
            self.is_terminal = True
        else:
            # TODO: use setdefault?
            if not self.has_child(word):
                self.create_child(word)

            self.get_child(word).insert_word(word[1:])

    def is_word(self, word: str):
        if len(word) == 0 and self.is_terminal:
            return True
        elif self.has_child(word):
            return self.get_child(word).is_word(word[1:])
        else:
            # Not a terminal and no child means this isn't a word
            return False

    def is_prefix(self, word: str):
        # If no letters left, this is the last node we'll check
        # Just need to know if this is terminal or if there are children
        if len(word) == 0 and (self.is_terminal or len(self.children) > 0):
            return True
        elif self.has_child(word):
            return self.get_child(word).is_prefix(word[1:])
        else:
            # Letters left in the word and no child and not terminal means this isn't a valid prefix
            return False

    def has_child(self, word):
        assert len(word) > 0, "Tried to find child for word with no characters"

        return word[0] in self.children

    def get_child(self, word):
        assert len(word) > 0, "Tried to get child for word with no characters"

        return self.children[word[0]]

    def create_child(self, word):
        assert len(word) > 0, "Tried to create child for word with no characters"

        self.children[word[0]] = Node()

