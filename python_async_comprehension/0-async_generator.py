#!/usr/bin/env python3
"""
Module that contains logic for async_generator coroutine
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    #  will yield float values, and will not receive/return any values
    """
    Function that will produce random number (1-10)
    for 10 occurrences with 1 second delay
    """
    for i in range(10):  # basic iteration
        await asyncio.sleep(1)  # force 1 second delay
        yield random.uniform(0, 10)  # yield (not return) random number 1-10
