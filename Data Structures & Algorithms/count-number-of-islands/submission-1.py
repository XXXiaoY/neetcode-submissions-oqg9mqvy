class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == '0':
                return
            if (i, j) in visited:
                return
            visited.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            return
        
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    count += 1
        return count
        