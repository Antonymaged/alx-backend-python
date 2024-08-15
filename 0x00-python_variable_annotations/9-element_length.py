#!/usr/bin/env python3

"""annotating the function’s parameters and return values"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """annotating the function’s parameters and return values"""
    return [(i, len(i)) for i in lst]
