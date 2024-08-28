#!/usr/bin/env python3
"""
Module contains async coroutine that contains function that waits
with random delay before returning

Caroutine - a function 'that can suspend its execution before reaching
its return and can pass control to another coroutine for some time
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for random delay between 0 and max_delay and returns the delay

    Args:
        max_delay (int): the maximum possible delay time (set to 10)

    Returns:
        float: the amount of delay time
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
