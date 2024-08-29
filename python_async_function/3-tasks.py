#!/usr/bin/env python3
"""
Module that contains function logic to create a task
(coroutine wrapper) which will run asynchronous function
"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes max_delay integer and returns a task that creates
    and runs the wait_random coroutine

    Args:
        max_delay (int): The maximum delay of the process

    Returns:
        asyncio.Task: A task object that allows for function
        execution
    """
    new_task = asyncio.create_task(wait_random(max_delay))
    return new_task
