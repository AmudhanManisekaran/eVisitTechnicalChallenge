from collections import defaultdict
from heapq import nlargest

# Class to track requests from IP addresses
class IPtracker:
    # Constructor function to initialize the cache that will store IP address along with request count
    def __init__(self):
        self.cache = defaultdict(int)

    # Function that handles requests made from IP addresses
    def request_handled(self, ip_address):
        self.cache[ip_address] += 1

    # Function that returns the top 100 IP addresses by request count, with the highest traffic IP address first
    def top100(self):
        currentCount = len(self.cache)
        N = min(currentCount, 100)
        highestTrafficIP = nlargest(N, self.cache, key = self.cache.get)
        return highestTrafficIP

    # Function that clears all the IP addresses and tallies
    def clear(self):
        self.cache.clear()
