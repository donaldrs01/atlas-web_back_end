#!/usr/bin/env python3
"""
Module that includes 'floor' fuction that takes float arg and returns the floor
"""
import math


def floor(n: float) -> int:
    """
    Returns the floor (rounds down to nearest integer)

    Args:
        n (float): the number to floor

    Returns:
        int: the floored number
    """
    return math.floor(n)
