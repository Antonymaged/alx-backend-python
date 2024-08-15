#!/usr/bin/env python3

import math

"""
This module returnes a floor for a float num
"""


def floor(n: float) -> int:
    """
    Returns the largest integer less than or equal to a given float.

    Args:
        n (float): The floating-point number to be floored.

    Returns:
        int: The floor of the number.

    Example:
        >>> floor(4.7)
        4
    """
    return math.floor(n)
