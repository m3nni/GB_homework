from typing import List


class Matrix:

    def __init__(self, matrix: List[List[int]]):
        if isinstance(matrix, list) and len(matrix) > 1:
            for i in matrix:
                if len(i) != len(matrix[0]):
                    raise ValueError('fail initialization matrix')
                else:
                    self.matrix = matrix
        else:
            raise ValueError('fail initialization matrix')

    def __str__(self) -> str:
        v_matrix = ''
        for i in self.matrix:
            v_matrix += f"| {str(i).strip('[]').replace(',', ' ')} |\n"
        return v_matrix

    def __add__(self, other):
        if len(self.matrix[0]) == len(other.matrix[0]):
            sum_matrix = Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                                 for i in range(len(self.matrix))])
        else:
            raise ValueError('Матрицы должны быть одной длинны')
        return sum_matrix


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
#    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
