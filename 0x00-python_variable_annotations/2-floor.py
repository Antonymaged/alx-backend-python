#!/usr/bin/env python3

import math

"""
This module provides a function to calculate the floor of a float number.
"""


def floor(n: float) -> int:
    """
     Returns the floor of a float number.

    Args:
        n (float): The float number to be floored.

    Returns:
        int: The largest integer less than or equal to `n`.

    Example:
        >>> floor(4.7)
        4
    """
    return math.floor(n)
