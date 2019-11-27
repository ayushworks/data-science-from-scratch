from chapter4.vector import Vector, dot_product, scalar_multiply, add, distance
from typing import Callable
import random


def sum_of_squares(v: Vector) -> float:
    """Computes the sum of squared elements in v"""
    return dot_product(v, v)


def different_quotient(f: Callable[[float], float],
                       x: float,
                       h: float) -> float:
    return (f(x+h) - f(x))/h


def partial_difference_quotient(f: Callable[[Vector], float],
                                v: Vector,
                                i: int,
                                h: float) -> float:
    """Returns the i-th partial difference quotient of f at v"""
    w = [v_j + (h if j == i else 0)    # add h to just the ith element of v
         for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h


def estimate_gradient(f: Callable[[Vector], float],
                      v: Vector,
                      h: float = 0.0001):
    return [partial_difference_quotient(f, v, i, h)
            for i in range(len(v))]


def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    """Moves `step_size` in the `gradient` direction from `v`"""
    assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)


def sum_of_squares_gradient(v: Vector) -> Vector:
    return [2 * v_i for v_i in v]


# pick a random starting point
point = [random.uniform(-10, 10) for i in range(3)]

print(point)

for epoch in range(1000):
    grad = sum_of_squares_gradient(point)    # compute the gradient at v
    point = gradient_step(point, grad, -0.01)    # take a negative gradient step
    print(epoch, point)

assert distance(point, [0, 0, 0]) < 0.001

inputs = [(x, 20*x +5) for x in range(-50, 50)]


def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    slope, intercept = theta
    predicted = slope*x + intercept
    error = (predicted - y)
    squared_error = error ** 2
    grad = [2*error*x, 2*x]
    return grad

