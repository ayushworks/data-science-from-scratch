from typing import List
import math


def sum_of_squares(xs: List[float]) -> float:
    return sum(x * x for x in xs)


def data_range(xs: List[float]) -> float:
    max(xs) - min(xs)


def mean_deviation(xs: List[float]) -> List[float]:
    mean = sum(xs)/len(xs)
    return [x - mean for x in xs]


def variance(xs: List[float]) -> float:
    """variance is sum of squares of deviations by length -1"""
    assert len(xs) >= 2
    return sum_of_squares(mean_deviation(xs))/(len(xs)-1)


def standard_deviation(xs: List[float]) -> float:
    """The standard deviation is the square root of the variance"""
    return math.sqrt(variance(xs))


num_friends = [5, 10, 15, 5, 10, 20, 10, 5]


print(variance(num_friends))
print(standard_deviation(num_friends))