#!/usr/bin/env python3
"""
Module that includes function definition for "to_kv"
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that takes string and either int/float and returns combo of args

    Args:
        k (str): the original str value
        v (Union[int, float]): num value (either int or float)

    Returns:
        Tuple[str, float]: combo of k/v values
    """
    return (k, float(v ** 2))  # square value of v
