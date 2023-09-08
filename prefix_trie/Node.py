from typing import Dict

from .WordContainer import WordContainer

class Node:
    def __init__(self):
        self.children: Dict[str, Node] = {}
        self.is_terminal = False

    def insert_word(self, word_container: WordContainer):
        if word_container.remaining_length() == 0:
            self.is_terminal = True
        else:
            # TODO: use setdefault?
            next_char = word_container.next_character()

            if not self.has_child(next_char):
                self.create_child(next_char)

            word_container.step()

            self.get_child(next_char).insert_word(word_container)

    def is_word(self, word: str):
        node = self.get_node(word)

        if node is None:
            return False

        return self.is_terminal

    def is_prefix(self, word: str):
        node = self.get_node(word)

        if node is None:
            return False

        # If no letters left, this is the last node we'll check
        # Just need to know if this is terminal or if there are children
        return node.is_terminal or len(node.children) > 0

    def get_node(self, word: str) -> 'Node':
        if len(word) == 0:
            return self
        elif self.has_child(word):
            return self.get_child(word).get_node(word[1:])
        else:
            # No valid path for this word
            return None

    def has_child(self, word):
        assert len(word) > 0, "Tried to find child for word with no characters"

        return word[0] in self.children

    def get_child(self, word) -> 'Node':
        assert len(word) > 0, "Tried to get child for word with no characters"

        return self.children[word[0]]

    def create_child(self, word):
        assert len(word) > 0, "Tried to create child for word with no characters"

        self.children[word[0]] = Node()

