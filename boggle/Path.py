from .Cell import Cell


class Path:
    def __init__(self, *, start: Cell = None):
        assert start is not None

        self.start = start
        self.cells = [start]
        self.cells_set = set(self.cells)

    def step(self, cell: Cell):
        assert cell not in self.cells_set, "Cannot step on same cell twice in the same path"

        self.cells.append(cell)
        self.cells_set.add(cell)

    def backtrack(self):
        assert len(self.cells) > 1, "Cannot backtrack path if only start has been stepped"

        removed = self.cells.pop()
        self.cells_set.remove(removed)

    def seen(self, cell: Cell):
        return cell in self.cells_set

    def current(self):
        return self.cells[-1]

    def word(self):
        return "".join(cell.letter for cell in self.cells)
