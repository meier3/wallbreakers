class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        squares = set()
        digits = n
        
        while True:
            # reset sum
            curr = 0
            
            # square & add each digit
            for d in str(digits):
                curr += int(d) ** 2
                
            # happy check
            if (curr == 1):
                return True
            elif (curr in squares):
                return False
            
            # update for next round
            digits = curr
            squares.add(curr)