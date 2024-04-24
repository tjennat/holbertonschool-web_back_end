#!/usr/bin/env python3
"""gonna measure time"""
import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


def measure_time(n: int, max_delay: int) -> float:
    """measure total time"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
