# Danica Meier 2019

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >= 2:
            n = n / 2.0
        
        return n == 1