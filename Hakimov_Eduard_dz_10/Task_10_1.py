from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        for i in range(len(matrix) - 1):
            if len(matrix[i]) != len(matrix[i + 1]):
                raise ValueError('fail initialization matrix')  # как то туго даются исключения, хотя в теории не так то и сложно
        self.matrix = matrix

    def __add__(self, other):
        matrix_result = [[num_1 + num_2 for num_1, num_2 in zip(list_1, list_2)]
                         for list_1, list_2 in zip(self.matrix, other.matrix)]
        matrix_result = Matrix(matrix_result)
        return matrix_result

    def __str__(self):
        result = ''
        for i in range(len(self.matrix)):
            result_str = f'\t|{" ".join(map(str, self.matrix[i]))}|\n'
            result += result_str
        return result


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
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
