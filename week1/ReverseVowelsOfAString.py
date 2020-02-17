        
        # cons = re.split('[aeiou]', s)
        # vowels = re.split('.^[aeiou]', s)
        # print(cons, '\n', vowels)

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        i = 0
        j = len(s) - 1
        chars = list(s)
        vowels = '[aeiouAEIOU]'
        
        while i < j:
            if not re.match(vowels, chars[i]):
                i += 1
            elif not re.match(vowels, chars[j]):
                j -= 1
            else:
                v1 = chars[i]
                v2 = chars[j]
                chars[i] = v2
                chars[j] = v1
                i += 1
                j -= 1
                
        return(''.join(chars))