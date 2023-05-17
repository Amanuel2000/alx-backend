#!/usr/bin/python3
""" 
A class called BasicCache that inherits from BaseCaching
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
        defineing class
    """

    def __init__(self):
        """
        super vlaue
        """
        super().__init__()
    
    def put(self, key, item):


        if key is None or item is None:
            pass
        else:
           if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data.keys():
               first_key = next(iter(self.cache_data.keys()))
               del self.cache_data[first_key]
               print("DISCARD: {}". format(first_key))
           self.cache_data[key] = item

 
    
    def get(self, key):

        """return the value of the data"""

        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)