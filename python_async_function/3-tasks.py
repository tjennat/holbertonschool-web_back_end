#!/usr/bin/env python3
"""task wait random func that takes int and return asyncio.Task"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """return asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
