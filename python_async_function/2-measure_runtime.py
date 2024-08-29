#!/usr/bin/env python3
"""
Module that contains function definition for 'measure_time' function
that will measure total execution time of wait_n function
"""
import asyncio
import time
import random
from typing import List
wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Function that measures and returns the amount of time
    for the wait_n function to execute

    Args:
        n (int): the number of wait_n occurrences
        max_delay (int): maximum delay time of each occurrence

    Returns:
        float: tatal execution time
    """
    start_time = time.time()  # measure starting time
    await wait_n(n, max_delay)  # execute wait_n
    end_time = time.time()  # record time after wait_n finishes process

    total_time = end_time - start_time
    return total_time / n  # returns average delay time
