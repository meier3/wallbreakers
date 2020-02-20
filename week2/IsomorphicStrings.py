class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # set up dict 
        charMap = {}
        reverseMap = {}
        n = len(s)
        
        # iterate through characters
        for i in range(n):
            charS = s[i]
            charT = t[i]
            # if current characters conflict with mapping, fail
            if ((charS in charMap) and (charMap[charS] != charT)) or ((charT in reverseMap) and (reverseMap[charT] != charS)):
                return False
            # update mapping 
            else:
                charMap[charS] = charT
                reverseMap[charT] = charS
        
        return True