// Danica Meier 2019

class Solution {
public:
    bool isPalindrome(string s) {
        
        while (s.length() > 1) {
            
            // remove chars if not alphanumeric, start over
            if (!isalnum(s.front())) {
                s.erase(s.begin());
                continue;
            }
            else if (!isalnum(s.back())) {
                s.pop_back();
                continue;
            }
            
            // compare outer chars
            if (tolower(s.front()) == tolower(s.back())) {
                s = s.substr(1, s.length()-2);
            }
            else 
                return false;
            
        }
        
        return true;
        
    }
};