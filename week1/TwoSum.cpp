// Danica Meier 2019

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        // test each number combination
        for (int i=0, n=nums.size(); i < n; i++) {
            
            int x = target - nums.at(i);
            
            for (int j = (i+1); j < n; j++) {
                if (nums.at(j) == x)  {
                    return vector<int> { i, j };
                }
            }
        }
        
        // in case there is no solution
        cout << "Solution not found." << endl;
        return vector<int> {0};
    }
};