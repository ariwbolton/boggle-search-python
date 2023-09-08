class WordContainer:
    def __init__(self, word: str):
        self.word = word
        self.length = len(word)
        self.index = 0

    def next_character(self):
        return self.word[self.index]

    def remaining(self):
        return self.word[self.index:]

    def remaining_length(self):
        return self.length - self.index

    def step(self):
        self.index += 1

