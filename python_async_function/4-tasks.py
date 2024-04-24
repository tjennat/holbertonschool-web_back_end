#!/usr/bin/env python3
"""altering the task_wait_n func"""
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returning the list of delay_l"""
    delay_l = []
    for _ in range(1, n + 1):
        delay_l.append(await task_wait_random(max_delay))
    for i in range(1, n):
        cle = delay_l[i]
        j = i - 1
        while j >= 0 and delay_l[j] > cle:
            delay_l[j + 1] = delay_l[j]
            j -= 1
        delay_l[j + 1] = cle
    return delay_l
