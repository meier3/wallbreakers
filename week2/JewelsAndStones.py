# Danica Meier 2019

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = set()
        numJ = 0

        for char in J:
            jewels.add(char)
        
        for stone in S:
            if stone in jewels:
                numJ += 1
        
        return numJ