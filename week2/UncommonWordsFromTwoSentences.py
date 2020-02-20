class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        from collections import defaultdict
        
        # split words, set up dict and output list
        words = A.split(' ') + B.split(' ')
        d = defaultdict(lambda: 0)
        uncommon = set()
        
        # tally word instances
        for w in words:
            d[w] += 1
            
        # collect uncommon words in output list
        for k in d.keys():
            if d[k] == 1:
                uncommon.add(k)
        
        # return final list
        return uncommon