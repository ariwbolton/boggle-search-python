from .PrefixTrie import PrefixTrie


class Visitor:
    def __init__(self, *, start: str = None, trie: PrefixTrie = None):
        self.start = start
        self.trie = trie
        self.nodes = [trie.root.get_node(start)]

    def current(self):
        return self.nodes[-1]

    def can_visit(self, char: str):
        return self.current().has_child(char)

    def step(self, char: str):
        self.nodes.append(self.current().get_node(char))

    def backtrack(self):
        self.nodes.pop()

