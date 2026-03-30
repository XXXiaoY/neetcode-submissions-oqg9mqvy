class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        row_l = len(grid)
        col_l = len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= row_l or j < 0 or j >= col_l or grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0
            visited.add((i ,j))
            count = dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i - 1, j)
            return count
        
        for i in range(row_l):
            for j in range(col_l):
                if grid[i][j] == 1:
                    return dfs(i ,j)
        return 0
 
        