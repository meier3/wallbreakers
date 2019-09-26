// Danica Meier

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        
        // iterate backwards through the vector
        vector<int>::iterator it = digits.end();

        while (*(--it) == 9) {
            
            // replace 9 with 0
            *it = 0;
            
            // increase vector size if carry over is necessary
            if (it == digits.begin()) {
                digits.insert(it++, 0);
                it = digits.begin()+1;
            }
        }

        // increase (or carry over)
        (*it)++;
     
        return digits;
    }
    
};