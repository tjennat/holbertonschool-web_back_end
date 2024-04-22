#!/usr/bin/python3
"""function that multiplies a float by multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that multiplies a float by multiplier."""
    def multiply(num: float) -> float:
        """return the product of num and multiplier"""
        return num * multiplier
    return multiply
