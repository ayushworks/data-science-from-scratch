from typing import Tuple
from typing import List
from typing import Callable

Matrix = List[List[float]]
Vector = List[float]


def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (# of rows of A, # of columns of A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of A (as a Vector)"""
    return A[i]


def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j th column of A (as a Vector)"""
    return [A_i[j] for A_i in A]


def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Returns a num_rows x num_cols matrix
    whose (i,j)-th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j) for j in range(num_cols)]
            for i in range(num_rows)]


def identity_matrix(size: int) -> Matrix:
    return make_matrix(size, size, lambda i, j: 0 if (i != j) else 1)


assert shape([[1, 2, 3, 4], [1, 2, 5, 6]]) == (2, 4)

assert get_row([[1, 2], [3, 4]], 1) == [3, 4]

assert get_column([[1, 2], [3, 4]], 1) == [2, 4]

assert make_matrix(2, 2, lambda i, j: i + j) == [[0, 1], [1, 2]]

assert identity_matrix(3) == [[1, 0, 0],
                              [0, 1, 0],
                              [0, 0, 1]]

