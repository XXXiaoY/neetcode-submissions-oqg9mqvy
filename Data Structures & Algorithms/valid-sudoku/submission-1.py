class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        c_set = defaultdict(list)
        r_set = defaultdict(list)
        s_set = defaultdict(list)
        r_l = len(board)
        c_l = len(board[0])

        for i in range(r_l):
            for j in range(c_l):
                cur = board[i][j]
                if cur != '.':
                    if cur in c_set[j]:
                        return False
                    else:
                        c_set[j].append(cur)
                    if cur in r_set[i]:
                        return False
                    else:
                        r_set[i].append(cur)
                    if cur in s_set[(i // 3, j // 3)]:
                        return False
                    else:
                        s_set[(i // 3, j // 3)].append(cur)
        return True