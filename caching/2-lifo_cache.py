#!/usr/bin/python3
"""
LIFO Cache module implementation
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Caching system that using LIFO (last in, first out)
    and inherits properties from BaseCaching
    """
    def __init__(self):
        """
        Initialize cache system using LIFO logic
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
            # If the key already exists, remove from stack
            if key in self.cache_data:
                self.key_stack.remove(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    last_key = self.key_stack.pop()  # remove last element
                    del self.cache_data[last_key]
                    print("DISCARD:", last_key)
            
            self.cache_data[key] = item  # add new item to cache
            self.key_stack.append(key)  # add new key to key_stack

    def get(self, key):
        """
        Function to retrieve item based on key value

        Args:
            key: the key value of the item to be retrieved
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
