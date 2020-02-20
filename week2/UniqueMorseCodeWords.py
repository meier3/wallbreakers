class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morseDict = { chr(97 + x) : morse[x] for x in range(26) }
        
        found = set()
        
        for w in words:
            trans = ''
            for c in w:
                trans += morseDict[c]
            found.add(trans)
            
        return len(found)