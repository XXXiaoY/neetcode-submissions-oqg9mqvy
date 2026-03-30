class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 准备三个“记录本”，记录数字是否出现过
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # key 是 (r//3, c//3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # 如果是空格，跳过
                if val == ".":
                    continue
                
                # 检查逻辑：
                # 1. 该行是否有重复
                # 2. 该列是否有重复
                # 3. 该 3x3 方块是否有重复
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[(r // 3, c // 3)]):
                    return False
                
                # 如果没重复，把数字记在账本上
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)
                
        return True
        