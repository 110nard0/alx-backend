#!/usr/bin/python3
"""LIFOCache module"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache is a caching system that stores key:value pairs in a
    public instance dictionary using the Last-In:First-Out algorithm
    """
    def __init__(self):
        """Initializes LIFOCache instance
        """
        super().__init__()
        self.last_item = ''

    def put(self, key: any, item: any):
        """Assigns to the instance dictionary the item value for the key
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.cache_data:
                last_item = self.last_item
                print(f'DISCARD: {last_item}')
                del self.cache_data[last_item]
            self.cache_data[key] = item
            self.last_item = key
        else:
            pass

    def get(self, key: any) -> any:
        """Returns the value in the instance dictionary linked to key
        """
        if key is None or not self.cache_data.get(key):
            pass
        else:
            return self.cache_data.get(key)
