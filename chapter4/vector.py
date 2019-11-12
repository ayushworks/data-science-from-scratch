from typing import List
import math

Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    # Check that vectors is not empty
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    # the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """multiply every element by c"""
    return [c * v_i for v_i in v]


def vector_mean(v: List[Vector]) -> Vector:
    """Compute the element wise average"""
    n = len(v)
    return scalar_multiply(1 / n, vector_sum(v))


def dot_product(v: Vector, w: Vector) -> float:
    """Compute dot product i.e v1*w1 + v2*w2"""
    assert len(v) == len(w)
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return dot_product(v, v)


def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))  # math.sqrt is square root function


def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(subtract(v, w))


def distance(v: Vector, w: Vector) -> float:
    return math.sqrt(squared_distance(v, w))


assert add(['a', 3], ['b', 90]) == ['ab', 93]

assert subtract([10, 10], [5, 5]) == [5, 5]

assert vector_sum([[1, 2, 3], [1, 2, 3]]) == [2, 4, 6]

assert scalar_multiply(2, [10, 5, 6]) == [20, 10, 12]

assert vector_mean([[4, 5, 6], [4, 5, 6]]) == [4.0, 5.0, 6.0]

assert dot_product([1, 2], [3, 4]) == 11

assert sum_of_squares([1, 2]) == 5

assert magnitude([3, 4]) == 5
