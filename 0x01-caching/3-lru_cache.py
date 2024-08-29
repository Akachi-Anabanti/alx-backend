#!/usr/bin/env python3
'''A file that defines a LRU class for caching'''

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Implements the LRU caching system"""

    def __init__(self):
        self.__rank = 0  # initial rank
        self.__rank_data = {}  # a dictionary to monitor the rank

        super().__init__()

    def put(self, key, item):
        """Assigns item to key in self.cache_data"""

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            sorted_rank = dict(sorted(self.__rank_data.items(),
                                      key=lambda item: item[1],
                                      reverse=True))

            least_recent_key, _ = sorted_rank.popitem()

            _ = self.cache_data.pop(least_recent_key)
            self.__rank_data = sorted_rank

            print(f"DISCARD: {least_recent_key}")

        self.cache_data[key] = item

        # monitoring and updating ranks
        if len(self.__rank_data) > 0:
            self.__rank += 1
        self.__rank_data[key] = self.__rank

    def get(self, key):
        """returns the item associated with key else none"""
        if key:
            # for every access increment the rank
            if self.__rank_data.get(key):
                self.__rank += 1
                self.__rank_data[key] = self.__rank
            return self.cache_data.get(key)
        return None
