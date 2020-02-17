# Danica Meier 2019

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import queue 

        q = queue.Queue()
        
        # store edge indices
        if len(board) > 0:
            lastRow = len(board) - 1
            lastCol = len(board[0]) - 1
        else:
            return
        
        # iterate over top/bottom edges
        for i in range(lastCol+1):
            # top edge
            if board[0][i] == 'O':
                q.put((0,i))
                board[0][i] = '1'
            # bottom edge
            if board[lastRow][i] == 'O':
                q.put((lastRow,i))
                board[lastRow][i] = '1'
        
        # iterate over side edges
        for row in range(lastRow+1):
            # left edge
            if board[row][0] == 'O':
                q.put((row,0))
                board[row][0] = '1'
            # right edge
            if board[row][lastCol] == 'O':
                q.put((row,lastCol))
                board[row][lastCol] = '1'
                
        # bfs
        while not q.empty():
            curr = q.get()
            nbs = []
            # find neighbors
            if curr[0] > 0:
                nbs.append((curr[0]-1, curr[1]))
            if curr[1] > 0:
                nbs.append((curr[0], curr[1]-1))
            if curr[0] < lastRow:
                nbs.append((curr[0]+1, curr[1]))
            if curr[1] < lastCol:
                nbs.append((curr[0], curr[1]+1))
            # check neighbors
            for nb in nbs:
                if board[nb[0]][nb[1]] == 'O':
                    q.put(nb)
                    board[nb[0]][nb[1]] = '1'
        
        # reset remaining Os
        for r in range(lastRow+1):
            for c in range(lastCol+1):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '1':
                    board[r][c] = 'O'