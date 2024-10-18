#!/usr/bin/env python3
"""Module for asynchronous tasks."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute task_wait_random 'n' times concurrently.

    Args:
        n (int): The number of times to execute task_wait_random.
        max_delay (int): The maximum random delay in seconds.

    Returns:
        List[float]: A sorted list of delay times (floats).
    """
    delays: List[float] = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return sorted(delays)
