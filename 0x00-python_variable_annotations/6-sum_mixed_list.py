#!/usr/bin/env python3

"""in this module the funvtion take list of int and floats and sum them"""
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """in this function it takes a list of int and float and return the sum"""
    return float(sum(mxd_lst))
