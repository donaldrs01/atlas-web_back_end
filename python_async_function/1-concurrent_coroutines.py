#!/usr/bin/env python3
"""
Module that contains logic to call wait_random multiple times
based on input 'n'
"""
import asyncio
import random
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    # return list of float numbers
    """
    Function receives 'n' input which is number of times to run wait_random

    Args:
        n (int): number of occurrences of wait_random
        max_delay (int): maximum wait time of each function call

    Returns:
        List[float]: a list of all the delay times (list of floats)
    """
    delay_times: List[float] = []  # initialize empty array for values
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delay_times.append(delay)  # appends each recorded delay time to list

    return delay_times
