#!/usr/bin/env python3
""" measure runtime"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    This function will execute the wait_n coroutine
    n times in parallel using asyncio.gather and measure
    the total execution time.
    """
    start_time = time.time()
    await asyncio.gather(*(wait_n(n, max_delay) for _ in range(n)))
    end_time = time.time()
    return (end_time - start_time) / n
