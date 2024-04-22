#!/usr/bin/python3
"""function that returns the length of a list"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    """return a list of tuples, a sequence and its length"""
    return [(i, len(i)) for i in lst]
