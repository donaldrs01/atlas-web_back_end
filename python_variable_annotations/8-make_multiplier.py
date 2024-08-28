#!/usr/bin/env python3
"""
Module that includes function definition for make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    # Callable tells us that return function takes a float and returns a float
    """
    Takes multiplier value as arg - returns function that multiplies
    another float value by multiplier

    Args:
        multiplier (float): the value of the mulitplier

    Returns:
        Callable[[float], float]: return function that multiplies float by mult
    """
    def return_function(a: float) -> float:
        return a * multiplier
    return return_function
