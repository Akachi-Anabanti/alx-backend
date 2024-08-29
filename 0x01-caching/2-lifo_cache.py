#!/usr/bin/env python3
'''A file that defines a LIFO class for caching'''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Implements the LIFO caching system"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Assigns item to key in self.cache_data"""

        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            last_in_key, _ = self.cache_data.popitem()
            # remove and return last in key, and item
            print(f"DISCARD: {last_in_key}")
        self.cache_data[key] = item

    def get(self, key):
        """returns the item associated with key else none"""
        if key:
            return self.cache_data.get(key)
        return None
