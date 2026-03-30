class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        row_l = len(grid)
        col_l = len(grid[0])
        
        def bfs(i, j):
            ans = 0
            q = deque([(i,j)])
            visited.add((i, j))
            ans = 0
            while q:
                r, c = q.popleft()
                for m, n in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    i_c = m + r
                    j_c = n + c
                    if i_c< 0 or i_c >= row_l or j_c < 0 or j_c >= col_l or grid[i_c][j_c] == 0:
                        ans += 1
                    elif (i_c, j_c) not in visited:
                        visited.add((i_c, j_c))
                        q.append((i_c, j_c))
            return ans
                
                


        
        for i in range(row_l):
            for j in range(col_l):
                if grid[i][j] == 1:
                    return bfs(i ,j)
        return 0
 
        