class Solution {
public:
    
    int explore (int i, int j, vector<vector<char>>& grid, vector<vector<bool>>& visited) {
        if (visited.at(i).at(j)) return 0;
        // mark visited
        visited.at(i).at(j) = 1;
        // if 1, explore neighbors
        if (grid.at(i).at(j) == '1') {
            // check nbs, explore if also 1
            if (i > 0) 
                explore(i-1, j, grid, visited);
            if (i < grid.size()-1)
                explore(i+1, j, grid, visited);
            if (j > 0)
                explore(i, j-1, grid, visited);
            if (j < grid.at(0).size()-1)
                explore(i, j+1, grid, visited);
            return 1;
        }
        // if 0, ignore
        return 0;
    }
    
    int numIslands(vector<vector<char>>& grid) {
        
        if (grid.empty()) return 0;
        
        int row_num = grid.size();
        int row_size = grid.at(0).size();
        
        int isles = 0;
        
        vector<vector<bool>> visited (row_num, vector<bool> (row_size, 0));
        
        for (int i=0; i < row_num; i++) {
            for (int j=0; j < row_size; j++) {
                
                if (! visited.at(i).at(j)) {
                    isles += explore(i, j, grid, visited);
                }
            }
        }
        
        return isles;
        
    }
};