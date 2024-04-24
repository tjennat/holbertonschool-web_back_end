#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return list of all delay in asc order"""
    delay_l = []
    for _ in range(1, n + 1):
        delay_l.append(await wait_random(max_delay))
    for i in range(1, n):
        cle = delay_l[i]
        j = i - 1
        while j >= 0 and delay_l[j] > cle:
            delay_l[j + 1] = delay_l[j]
            j -= 1
        delay_l[j + 1] = cle
    return delay_l
