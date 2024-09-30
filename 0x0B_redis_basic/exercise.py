#!/usr/bin/env python3
"""
Module for beginning exercises using redis
"""
import redis
import uuid
from typing import Union


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
