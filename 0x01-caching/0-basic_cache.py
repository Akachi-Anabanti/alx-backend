#!/usr/bin/env python3
'''A file that contains a baisc cache class definition
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Defines a Basic Caching system"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Assigns to the dict self.cache_data the
        value and item"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """returns the item assigned to a key"""
        if key is not None:
            return self.cache_data.get(key)
