#!/usr/bin/env python3
"""gonna measure time"""
import asyncio
import random


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure total time"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    end_total = end_time - start
    return float(end_total / n)
