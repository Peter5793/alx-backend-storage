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

    def get(self, key: str, fn: Callable = None)\
            -> Union[str, bytes, int, float]:
        """
        store the cache
        args: bring informatiion to store
        Return: key or number uuid
        """
        key = self._redit.get(key)

        if fn:
            return fn(key)

        return key

    def get_str(self, key:str) -> str:
        """ parametrized get str"""
        return self._redit.get(key).decode("utf-8")

    def get_int(self, key:str) -> int:
        """parametrized get int"""
        value = self.redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0

        return value
