#!/usr/bin/env python3
"""
Module for beginning exercises using redis
"""
import redis
import uuid
from typing import Union, Callable, Optional


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
