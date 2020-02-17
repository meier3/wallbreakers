class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        words = s.split(' ')
        output = []
        
        for w in words:
            chs = list(w)
            chs.reverse()
            output.append(''.join(chs))
            
        return ' '.join(output)