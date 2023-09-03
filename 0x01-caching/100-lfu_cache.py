#!/usr/bin/python3
"""LFUCache module"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFUCache is a caching system that stores key:value pairs in a
    public instance dictionary using the Least Frequently Used algorithm
    """
    def __init__(self):
        """Initializes LFUCache instance
        """
        super().__init__()
        self.usage_list = []
        self.usage_dict = {}

    def put(self, key: any, item: any):
        """Assigns to the instance dictionary the item value for the key
        """
        if key and item:
            length = len(self.cache_data)
            if length == BaseCaching.MAX_ITEMS and key not in self.cache_data:
                least_freq = min(self.usage_dict.values())
                lfu_items = [k for k, v in self.usage_dict.items()
                             if v == least_freq]
                if len(lfu_items) == 1:
                    least = lfu_items[0]
                    print(f'DISCARD: {least}')
                    del self.cache_data[least]
                    del self.usage_dict[least]
                    self.usage_list.remove(least)
                else:
                    positions = [self.usage_list.index(item)
                                 for item in lfu_items]
                    least_used = min(positions)
                    least = self.usage_list[least_used]
                    print(f'DISCARD: {least}')
                    del self.cache_data[least]
                    del self.usage_dict[least]
                    del self.usage_list[self.usage_list.index(least)]
            self.cache_data[key] = item
            self.usage_dict[key] = self.usage_dict.get(key, 0)
            self.usage_dict[key] += 1
            if key in self.usage_list:
                del self.usage_list[self.usage_list.index(key)]
            self.usage_list.append(key)
        else:
            pass

    def get(self, key: any) -> any:
        """Returns the value in the instance dictionary linked to key
        """
        if key is not None and self.cache_data.get(key):
            del self.usage_list[self.usage_list.index(key)]
            self.usage_list.append(key)
            self.usage_dict[key] += 1
            return self.cache_data.get(key)
        return None
