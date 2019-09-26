// Danica Meier 2019

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {

        bool failed = false;
        string prefix = "";
        int n = strs.size();
        
        // exit if input is empty
        if (n == 0) return prefix;
        
        // iterate through characters in first string
        for (int i = 0, len = strs.at(i).length(); i < len; i++) {
            
            char c = strs.at(0)[i];
            
            // compare char with same index of every other string
            // (comparing all words, one char at a time)
            for (int j = 1; j < n; j++) {
                if (strs.at(j)[i] != c) {
                    failed = true;
                    break;
                }
            }
            
            // if not failed, record char and continue
            if (failed) break;
            prefix += c;
        }
        return prefix;
    }
};