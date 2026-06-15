class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        already = set()
        
        for i in range(row):
            for j in range(col):
                val = board[i][j]
                if val == '.':
                    continue
                if (i, 'row', val) in already or (j, 'col', val) in already or (i//3, j//3, val) in already:
                    return False
                else:
                    already.add((i, 'row', val))
                    already.add((j,'col',val))
                    already.add((i//3, j//3, val))
        
        return True

        