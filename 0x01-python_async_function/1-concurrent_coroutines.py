#!/usr/bin/env python3
""" wait number"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times concurrently and returns
    a sorted list of delays.

    Args:
        n (int): The number of times to execute wait_random.
        max_delay (int): The maximum random delay in seconds
        for each wait_random call.

    Returns:
        List[float]: A sorted list of delay times (floats).
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    delays.sort()
    return delays
