#!/usr/bin/python3
"""
MRU (most recently used) cache model implementation
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Caching system that uses MRU (most recently used)
    logic and inherits properties from BaseCaching
    """
    def __init__(self):
        """
        Initialize cache system using LRU logic
        """
        super().__init__()  # call init method of parent class
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Function to add items into cache
        If exceeding limit, will remove MRU item
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # mark key as recently used by moving to end
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = next(reversed(self.cache_data))  # retrieve last key (MRU)
            del self.cache_data[last_key]
            print("DISCARD:", last_key)

    def get(self, key):
        """
        Function to retrieve item based on key value

        Args:
            key: the key value of the item to be retrieved
        """
        if key is None or key not in self.cache_data:
            return None
        #  move key to end of list to mark as recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
