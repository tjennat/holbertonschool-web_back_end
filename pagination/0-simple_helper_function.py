#!/usr/bin/env python3
"""Module containing index_range"""


def index_range(page: int, page_size: int) -> tuple:
    """func that's gonna return the start of index and the end"""
    start = (page - 1) * page_size
    end = start + page_size

    return start, end
