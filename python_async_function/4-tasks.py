#!/user/bin/env python3
"""altering the task_wait_n function"""

from typing import List
import asyncio
import random


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returning delays."""
    lists_task = []
    for _ in range(n):
        task = asyncio.create_task(task_wait_random(max_delay))
        lists_task.append(task)
    delays = await asyncio.gather(*lists_task)
    for i in range(len(delays)):
        for j in range(len(delays) - 1):
            if delays[j] > delays[j + 1]:
                temp = delays[j]
                delays[j] = delays[j + 1]
                delays[j + 1] = temp
    return delays
