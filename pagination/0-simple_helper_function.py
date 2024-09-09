#!/usr/bin/env python3
"""
Module for function index_range
"""


def index_range(page: int, page_size: int) -> tuple:
    """Function that provides tuple providing start_index of page
    and the end_index of the page
    """
    start_index = (page - 1) * page_size
    #  start index defined by page number - 1 (0 index)
    #  multiplied by the number of items on page
    end_index = start_index + page_size
    #  end index defined by + 10 from start_index of page
    return (start_index, end_index)
