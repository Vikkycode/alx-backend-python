#!/usr/bin/env python3
""" async generator"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This coroutine will loop 10 times, each time asynchronously
    a wait 1 second then yield a random number between 0 and 10.
    """
    return [number async for number in async_generator()]