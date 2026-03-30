class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])

        def dfs(i, j):
            if 0 <= i < row and 0 <= j < col and grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
                return
            return


        count = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count




        