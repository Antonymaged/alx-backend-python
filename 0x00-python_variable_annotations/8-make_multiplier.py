#!/usr/bin/env python3

"""in this module we use the call back to call a func inside another"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function that multiplies a float multiplier

    Parameters:
    multiplier (float): The multiplier value.

    Returns:
    Callable[[float], float].

    Example:
    >>> multiply_by_3 = make_multiplier(3.0)
    >>> multiply_by_3(4.0)
    12.0
    """
    return lambda x: x * multiplier
