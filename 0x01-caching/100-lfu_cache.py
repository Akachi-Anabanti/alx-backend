#!/usr/bin/env python3
'''A file that defines a LFU class for caching'''

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Implements the LRU caching system"""

    def __init__(self):
        self.__rank = 0
        self.__lfu_data = {}  # a dictionary to monitor the freq

        super().__init__()

    def put(self, key, item):
        """Assigns item to key in self.cache_data"""

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:

            sorted_lfu_data = dict(sorted(self.__lfu_data.items(),
                                          key=lambda item: (
                                                            item[1]["freq"],
                                                            item[1]['rank']
                                                            ),
                                          reverse=True))

            least_freq_key, _ = sorted_lfu_data.popitem()

            del self.cache_data[least_freq_key]
            del self.__lfu_data[least_freq_key]

            print(f"DISCARD: {least_freq_key}")

        self.cache_data[key] = item

        if len(self.__lfu_data) > 0:
            self.__rank += 1
        # monitoring and updating ranks
        self.__lfu_data[key] = {"freq": 0, "rank": self.__rank}

    def get(self, key):
        """returns the item associated with key else none"""
        if key in self.cache_data.keys():
            self.__lfu_data[key]["freq"] += 1
            self.__rank += 1
            self.__lfu_data[key]["rank"] = self.__rank
            return self.cache_data.get(key)
        return None
