class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen =set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == '.':
                    continue
                
                box = (r//3)*3 + (c//3)
                
                row_tuple = ("r", r, val)
                col_tuple = ("c", c, val)
                box_tuple = ("b", box, val)
                
                if row_tuple in seen or col_tuple in seen or box_tuple in seen:
                    return False
                
                seen.add(row_tuple)
                seen.add(col_tuple)
                seen.add(box_tuple)

        return True