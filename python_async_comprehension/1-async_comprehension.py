#!/usr/bin/env python3
"""
Module that contains logic for async comprehension over
async_generator and the 10 randomly generated numbers
"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Function that performs comprehension on randomly generated
    numbers

    Returns:
        List[float]: a list of the RGNs
    """
    result = [num async for num in async_generator()]
    return result
