class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(i, j):
            if i in range(rows) and j in range(cols) and grid[i][j] == '1':
                grid[i][j] = 0
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
            return

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' :
                    count += 1
                    dfs(i, j)
                   
        
        return count

        