class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        d = {}
        words = s.split(' ')
        n = len(pattern)
        
        if (n != len(words)): 
            return False
        
        for i in range(n):
            key = pattern[i]
            w = words[i]
            if (not key in d):
                if (not w in d.values()):
                    d[key] = w
                else:
                    return False
            elif not d[key] == w:
                return False
            
        return True