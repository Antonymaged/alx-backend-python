#!/usr/bin/env python3

"""Given the parameters and the return values"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """Retrieves a using a key"""
    if key in dct:
        return dct[key]
    else:
        return default
