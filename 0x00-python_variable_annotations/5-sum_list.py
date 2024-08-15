#!/usr/bin/env python3

"""in this module it returens the sum of floats in a list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all float elements in a list.

    Parameters:
    lis (list of float): A list containing float numbers.

    Returns:
    float: The sum of all float numbers in the list.

    Example:
    >>> sum_list([1.0, 2.5, 3.0])
    6.5
    """
    sum: float = 0
    for i in lis:
        sum += i
    return sum
