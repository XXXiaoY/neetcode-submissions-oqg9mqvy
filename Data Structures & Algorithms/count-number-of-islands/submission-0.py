class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            # 1. 终止条件（出界或者是水）
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # 2. 标记当前格子为已访问（把陆地变水，防止死循环）
            grid[r][c] = '0'
            
            # 3. 向上下左右四个方向“传染”
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 主循环：遍历每一个格子
        for i in range(rows):
            for j in range(cols):
                # 每发现一块新的陆地，就是发现了一个新岛屿
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j) # 用 DFS 把这座岛全部“淹没”
        
        return count
        