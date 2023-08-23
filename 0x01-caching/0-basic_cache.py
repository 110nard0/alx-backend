#!/usr/bin/python3
"""BasicCache module"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache
    """
    def __init__(self):
        """Initializes BasicCache instance
        """
        super().__init__()

    def put(self, key: any, item: any):
        """Assigns to the instance dictionary the item value for the key
        """
        if key and item:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key: any) -> any:
        """Returns the value in the instance dictionary linked to key
        """
        if key is None or not self.cache_data.get(key):
            pass
        else:
            return self.cache_data.get(key)
