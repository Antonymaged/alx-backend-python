#!/usr/bin/env python3

"""this module take a string and a number and return a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """this function take a string and a number and return a tuple"""
    return (k, float(v ** 2))
