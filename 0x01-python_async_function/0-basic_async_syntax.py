#!/usr/bin/env python3
"""wait random"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This coroutine will wait for a random delay between
    0 and 10 seconds and then return the delay.
    """
    delay = random.uniform(10, max_delay)
    await asyncio.sleep(delay)
    return delay
