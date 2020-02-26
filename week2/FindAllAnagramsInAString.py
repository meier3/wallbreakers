class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        
        refSet = Counter(p)
        pattLen = len(p)
        anagrams = []
        strLen = len(s) - pattLen + 1
        
        if (strLen < pattLen):
            return anagrams
        
        for i, c in enumerate(s[:strLen]):
            
            if c in refSet:
                currentCount = Counter()
                found = True
                for j in range(pattLen):
                    currChar = s[i+j]
                    if (currentCount[currChar] >= refSet[currChar]):
                        found = False
                        break
                    else:
                        currentCount.update(currChar)
                if found:
                    anagrams.append(i)
                    
        return anagrams