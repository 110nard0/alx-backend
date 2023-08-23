#!/usr/bin/python3
"""FIFOCache module"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache is a caching system that stores key:value pairs in a
    public instance dictionary using the First In-First Out algorithm
    """
    def __init__(self):
        """Initializes FIFOCache instance
        """
        super().__init__()
        self.cache_list = []

    def put(self, key: any, item: any):
        """Assigns to the instance dictionary the item value for the key
        """
        if key and item:
            self.cache_data[key] = item           
            self.cache_list.append(key)
        else:
            pass

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item = self.cache_list[0]
            print(f'DISCARD: {first_item}')
            del self.cache_data[first_item]
            self.cache_list.remove(first_item)

    def get(self, key: any) -> any:
        """Returns the value in the instance dictionary linked to key
        """
        if key is None or not self.cache_data.get(key):
            pass
        else:
            return self.cache_data.get(key)
