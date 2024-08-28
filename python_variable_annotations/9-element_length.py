#!/usr/bin/env python3
"""
Module that includes function definition for element_length
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function takes list of sequences and returns a list of tuples
    Each tuple contains a sequence and its length (int)

    Args:
        lst (List[str]): List of sequences (strings, lists, tuples)

    Returns:
        List[Tuple[str, int]]: List of tuples - sequence / sequence length
    """
    return [(i, len(i)) for i in lst]
