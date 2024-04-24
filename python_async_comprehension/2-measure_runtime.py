#!/usr/bin/env python3
"""func coroutine that will execute async func four times in parallel."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the runtime and return it."""
    task = []
    start = time.time()
    for _ in range(4):
        task.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*task)
    end = time.time()
    return end - start
