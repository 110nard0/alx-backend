#!/usr/bin/python3
"""LRUCache module"""

from datetime import datetime

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache is a caching system that stores key:value pairs in a
    public instance dictionary using the Least Recently Used algorithm
    """
    def __init__(self):
        """Initializes LRUCache instance
        """
        super().__init__()
        self.cache_dict = {}

    def put(self, key: any, item: any):
        """Assigns to the instance dictionary the item value for the key
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.cache_data:
                least = min(self.cache_dict.values())
                for k, v in self.cache_dict.items():
                    if v == least:
                        least_recent = k
                print(f'DISCARD: {least_recent}')
                del self.cache_data[least_recent]
                del self.cache_dict[least_recent]
            self.cache_data[key] = item
            self.cache_dict[key] = datetime.now()
        else:
            pass

    def get(self, key: any) -> any:
        """Returns the value in the instance dictionary linked to key
        """
        if key is None or not self.cache_data.get(key):
            pass
        else:
            self.cache_dict[key] = datetime.now()
            return self.cache_data.get(key)
