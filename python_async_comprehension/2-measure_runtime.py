#!/usr/bin/env python3
"""
Module that contains logic for four parallel comprehensions
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of running async_comprehension
    four times in parallel executions

    Returns:
    -The total runtime in seconds (float)
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.perf_counter()

    run_time = end_time - start_time
    return run_time
