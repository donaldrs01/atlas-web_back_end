#!/usr/bin/env python3
"""
Module that includes function definition for 'sum_mixed_list'
"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function that takes a mixed list of args (ints and floats) and returns their sum
    Args:
        mxd_lst (List): a mixed list of ints and float ints

    Returns:
        float: the sum of the list as a float
    """
    return sum(mxd_lst)
