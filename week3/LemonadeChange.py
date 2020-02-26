class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        from collections import Counter
        
        if (bills[0] != 5):
            return False
        
        drawer = Counter()
        
        for b in bills:
            
            if (b == 5):
                drawer[5] += 1
                
            elif (b == 10):
                if (drawer[5] > 0):
                    drawer[5] -= 1
                    drawer[10] += 1
                else:
                    return False
                
            elif (b == 20):
                if (drawer[10] >= 1 and drawer[5] >= 1):
                    drawer[5] -= 1
                    drawer[10] -= 1
                    drawer[20] += 1
                elif (drawer[5] >= 3):
                    drawer[5] -= 3
                    drawer[20] += 1
                else:
                    return False
                
        return True