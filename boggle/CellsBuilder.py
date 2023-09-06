from itertools import product
from typing import List, Tuple, Union
from .Cell import Cell


class CellsBuilder:
    height: int
    width: int
    cells: List[List[Cell]]

    def build_cells(self, letters) -> List[List[Cell]]:
        self.height = len(letters)
        assert self.height > 0, "Height of board must be nonzero"

        self.cells = []

        for y, row in enumerate(letters):
            # TODO: Enable rectangles
            assert self.height == len(row), "All rows must have same length as height"

            self.width = len(row)

            self.cells.append([])

            for x, letter in enumerate(row):
                self.cells[-1].append(Cell(x=x, y=y, letter=letter))

        for y, row in enumerate(self.cells):
            for x, cell in enumerate(row):
                for neighbor_vec_direction in product((-1, 0, 1), (-1, 0, 1)):
                    if neighbor_vec_direction == (0, 0):
                        continue  # This is just the current cell, which is not it's own neighbor

                    neighbor = self.get_neighbor_cell(
                        cell,
                        neighbor_vec_direction=neighbor_vec_direction,
                    )

                    if neighbor:
                        cell.add_neighbor(neighbor)

        return self.cells

    def get_neighbor_cell(self, cell: Cell, neighbor_vec_direction: Tuple[int, int] = None) -> Union[Cell, None]:
        neighbor_x, neighbor_y = tuple(sum(values) for values in zip(cell.vec(), neighbor_vec_direction))

        if neighbor_x < 0 or neighbor_x >= self.width:
            return None
        if neighbor_y < 0 or neighbor_y >= self.height:
            return None

        return self.cells[neighbor_y][neighbor_x]
