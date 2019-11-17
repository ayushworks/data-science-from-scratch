from typing import List
from collections import Counter


def _median_odd(data: List[float]) -> float:
    """return mid point if no of elements are odd"""
    return sorted(data)[len(data) // 2]


def _median_even(data: List[float]) -> float:
    """return average of 2 middle points"""
    middle = len(data) // 2
    l = sorted(data)
    return (l[middle - 1] + l[middle]) / 2


def _median(data: List[float]) -> float:
    return _median_odd(data) if len(data) % 2 != 0 else _median_even(data)


assert _median([1, 10, 2, 9, 5]) == 5
assert _median([1, 9, 2, 10]) == (2 + 9) / 2


def quantile(xs: List[float], p: float) -> float:
    """return the pth percentile value in xs"""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index-1 if p_index == len(xs) else p_index]


num_friends = [5, 8, 10, 15, 20, 10, 15, 30, 20, 70, 70, 10, 20, 15, 15, 10, 20]

assert quantile(num_friends, 0.10) == 8
assert quantile(num_friends, 1) == 70


def mode(x: List[float]) -> List[float]:
    """Returns a list, since there might be more than one mode"""
    counts = Counter(x)
    max_counts = max(counts.values())
    return [x_i for x_i,count in counts.items()
            if count == max_counts]


assert mode(num_friends) == [10, 15, 20]