#!/usr/bin/python3
"""
BasicCache module implementation
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Caching system that inherits properties from BaseCaching parent class
    """
    def put(self, key, item):
        """
        Basic function that adds an item into cache

        Args:
            key: the key with which item is stored
            item: the value to be stored in cache associated with key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Function that returns the key value in order to get item
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
