#!/usr/bin/env python3
"""
Module that includes function definition for 'sum_list'
"""
from typing import List


def sum_list(input_list: List[float]) -> float:  # type List
    """
    Function that receives series of floats as args and returns their sum

    Args:
        input_list (float): a list of float ints

    Returns:
        float: sum of ints as a float
    """
    return sum(input_list)
