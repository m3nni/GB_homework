class Cell:

    def __init__(self, cells: int):
        if isinstance(cells, int):
            self.cells = cells
        else:
            raise TypeError("неверное значение Cells (должно быть целочисленное (int))")

    def make_order(self, number: int) -> str:
        base_str = f'{number * "*"}\n'
        other_str = f'{base_str * (self.cells // number)}'
        last_str = f'{"*" * (self.cells % number)}'
        return f'{other_str}{last_str}\n'

    def __add__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            add_cell: Cell = Cell(self.cells + other.cells)
        else:
            raise TypeError('действие допустимо только для экземпляров того же класса')
        return add_cell

    def __sub__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            if self.cells < other.cells:
                raise ValueError('недопустимая операция')
            else:
                sub_cell: Cell = Cell(self.cells - other.cells)
        else:
            raise TypeError('действие допустимо только для экземпляров того же класса')
        return sub_cell

    def __mul__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            mul_cell: Cell = Cell(self.cells * other.cells)
        else:
            raise TypeError('действие допустимо только для экземпляров того же класса')
        return mul_cell

    def __truediv__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            truediv_cell: Cell = Cell(int(self.cells / other.cells))
        else:
            raise TypeError('действие допустимо только для экземпляров того же класса')
        return truediv_cell

    def __floordiv__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            floordiv_cell: Cell = Cell(int(self.cells // other.cells))
        else:
            raise TypeError('действие допустимо только для экземпляров того же класса')
        return floordiv_cell


if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))
    """
    **********
    *****
    """

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))
    """
    ******
    ******
    *
    """

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))
    """
    ******
    ******
    """

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)  # 30

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)  # 3

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)  # 1

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)  # недопустимая операция

    try:
        cell_1 * 123
    except TypeError as err:
        print(err)  # действие допустимо только для экземпляров того же класса
