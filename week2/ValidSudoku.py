class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        from collections import defaultdict
        
        # store values in sets by row, col, box
        cols = defaultdict(lambda: set())
        rows = defaultdict(lambda: set())
        boxes = defaultdict(lambda: set())

        # iterate through cells 
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                # calculate current sub-box
                b = (c / 3) + (3 * (r / 3))
                # skip empty cell
                if (cell == '.'):
                    continue
                # validate cell
                elif cell in cols[c] or cell in rows[r] or cell in boxes[b]:
                    return False
                # update sets
                else:
                    cols[c].add(cell)
                    rows[r].add(cell)
                    boxes[b].add(cell)
                    
        return True