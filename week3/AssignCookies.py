class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        matched = 0
        
        g.sort()
        s.sort()
        
        while (len(g) > 0 and len(s) > 0):
            # most to least greedy
            greed = g.pop()
            size = s.pop()
            
            if (size >= greed):
                matched += 1
            elif (size < greed):
                s.append(size)
        
        return matched