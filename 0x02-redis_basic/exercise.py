#!/usr/bin/env python3
""" writing strings to Redis"""
from uuid import uuid4
from typing import Union, Callable
from functools import wraps
import redis


class Cache:
    """funtionality redis"""
    def __init__(self):
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ 
        store the cache
        args: data arguments
        return : strings
        """
        key =str(uuid4())
        self._redis.set(key, data)

        return key
