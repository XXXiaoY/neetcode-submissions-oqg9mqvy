class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, index):
            # 1. 成功：单词所有字母都匹配完了
            if index == len(word):
                return True
            
            # 2. 失败（剪枝）：出界、字母不匹配、或者已经访问过
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                board[r][c] != word[index]):
                return False
            
            # 3. 【做选择】：标记当前格子已访问
            # 技巧：不需要额外 set，直接修改原数组为一个特殊字符
            temp = board[r][c]
            board[r][c] = '#' 
            
            # 4. 【递归】：向四个方向搜索
            # 只要有一个方向通了，就返回 True
            res = (dfs(r+1, c, index+1) or 
                   dfs(r-1, c, index+1) or 
                   dfs(r, c+1, index+1) or 
                   dfs(r, c-1, index+1))
            
            # 5. 【回溯】：撤销选择，把格子还原
            board[r][c] = temp
            
            return res

        # 遍历棋盘，寻找起点
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False