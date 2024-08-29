#!/usr/bin/env python3
'''A file that defines a Fifo class for caching'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Implements the FIFO caching system"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Assigns item to key in self.cache_data"""

        if key is None or item is None:
            return
        if len(self.cache_data) > self.MAX_ITEMS:
            first_in_key = list(self.cache_data.keys())[0]
            _ = self.cache_data.pop(first_in_key)
            # remove and return first key, and item
            print(f"DISCARD: {first_in_key}")
        self.cache_data[key] = item

    def get(self, key):
        """returns the item associated with key else none"""
        if key:
            return self.cache_data.get(key)
        return None
