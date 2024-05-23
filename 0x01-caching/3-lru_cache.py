#!/usr/bin/python3
"""LRU Caching"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """class LRUCache"""
    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            re_key, re_value = self.cache_data.popitem(last=True)
            print(f"DISCARD: {re_key}")
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """ Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
