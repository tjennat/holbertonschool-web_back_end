#!/usr/bin/python3
"""function that's gonna return a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a tuple with a string and a float"""
    return (k, v * v)
