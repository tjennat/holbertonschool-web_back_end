#!/usr/bin/env python3
"""function that's gonna summarize a mix list of floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the sum of the list of floats"""
    return sum(mxd_lst)
