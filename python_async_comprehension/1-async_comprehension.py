#!/usr/bin/env python3
"""A coroutine"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """this is the coroutine async_generator."""
    return [i async for i in async_generator()]
