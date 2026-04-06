class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(list)
        row = defaultdict(list)
        box = defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == ".":
                    continue
                if val in col[j] or val in row[i] or val in box[(i//3, j//3)]:
                    return False
                else:
                    col[j].append(val)
                    row[i].append(val)
                    box[(i//3, j//3)].append(val)
        
        return True

        