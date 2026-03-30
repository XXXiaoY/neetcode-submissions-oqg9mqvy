class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_s = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i, j):
            if i in range(rows) and j in range(cols) and grid[i][j] == 1:
                grid[i][j] = 0
                return (1 +  dfs(i + 1, j) + dfs(i - 1, j) +  dfs(i, j + 1) + dfs(i, j - 1))
            return 0
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    a = dfs(i, j)
                    max_s = max(max_s, a)
                    
        return max_s
                        


        