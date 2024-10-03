#!/usr/bin/env python3
"""
Module for beginning exercises using redis
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

#  Defining decorator that takes method as argument and wraps
#  that method in a function that increments counter each time
#  particular method is used


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts # of times a specific method is called

    Args:
        method(Callabe): The method to wrap with the decorator
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper that increments the call count for given method
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorater that stores input/output keys of the decorated function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function to store input/output values
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        # Convert args to string format and push to input_key list
        self._redis.rpush(input_key, str(args))
        # Execute wrapped method and record output to output_key list
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


def replay(method):
    """
    Method that returns and displays the call_history list
    of inputs and outputs of particular function
    """
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"


class Cache:
    """
    Redis cache class
    """

    def __init__(self) -> None:
        """
        Initialize the Cache class and flush the DB
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    # Decoraters on store method)
    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in redis with random UUID key
        """
        key = str(uuid.uuid4())
        #  Store data in Redis as key-value pair
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """
        Retrieve data stored under key value from Redis
        """
        #  Retrieve data using .get
        data = self._redis.get(key)

        if data is None:
            return None
        #  Apply conversion function to data if inputted as arg
        if fn:
            return fn(data)
        #  Return raw data if no conversion function
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve and decode str value from Redis
        """
        data = self.get(key)
        return data.decode("utf-8") if data else None

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve and decode int value from Redis
        """
        data = self.get(key)
        return int(data) if data else None
