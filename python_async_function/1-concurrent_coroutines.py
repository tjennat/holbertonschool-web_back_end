#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""
import asyncio
import random
from typing import List


import wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns 'delay' times in asc order."""
    delay_l = []
    for _ in range(n):
        delay_l.append(wait_random(max_delay))
    time_length = await asyncio.gather(*delays)
    for i in range(len(time_length)):
        for j in range(len(time_length) - 1):
            if time_length[j] > time_length[j + 1]:
                temp = time_length[j]
                time_length[j] = time_length[j + 1]
                time_length[j + 1] = temp
    return time_length
