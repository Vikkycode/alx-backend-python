#!/usr/bin/env python3
""" measure runtime"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function will return the task
    """
    return asyncio.create_task(wait_random(max_delay))
