#!/usr/bin/env python3
"""function that returns the length of a list"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns values with their length in a list"""
    return [(i, len(i)) for i in lst]
