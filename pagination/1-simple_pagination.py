#!/usr/bin/env python3
"""
Module for index_range function with additional functionality
"""
import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Function that returns appropriate page of dataset
        based on page and page_size input

        Args:
            page (int): The page number. Defaults to 1.
            page_size (int): The number of items on page. Defaults to 10.

        Returns:
            List[List]: Correct list of rows of the dataset.
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        # use index_range function to determine start and end indexes
        start_index, end_index = index_range(page, page_size)

        data = self.dataset()

        #  determine if start_index is less than the number of rows of data
        if start_index < len(data):
            #  if so, return sliced dataset
            return data[start_index:end_index]
        else:
            return []
