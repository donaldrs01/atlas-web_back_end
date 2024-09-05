#!/usr/bin/python3
"""
FIFOCache module implementation
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Caching system that using FIFO (first in, first out)
    and inherits properties from BaseCaching
    """
    def __init__(self):
        """
        Initialize cache system using FIFO logic
        """
        super().__init__()
        self.key_stack = []  # initialize empty array to hold keys in order

    def put(self, key, item):
        """
        Function to add items into cache.
        Will remove first cached item if over limit

        Args:
            key: key that references the stored item
            item: value associated with stored key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item  # add item to cache
            self.key_stack.append(key)  # add item to key_stack array

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.key_stack.pop(0)  # remove first-in cache item
            del self.cache_data[first_key]
            print("DISCARD:", first_key)

    def get(self, key):
        """
        Function to retrieve item based on key value

        Args:
            key: the key value of the item to be retrieved
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
