// Danica Meier 2019

class Solution {
public:
    int titleToNumber(string s) {
        
        int sum = 0;

        // calculate value of each character from least to most significant
        for (int i=0, len=s.length(); i < len; i++) {    
            // get character
            char c = s[len-i-1];
            
            // get letter value from ascii
            int val = int(c) - 64;
            
            // calculate digit value
            sum += (pow(26,i) * val);
        }
        
        return sum;
    }
};