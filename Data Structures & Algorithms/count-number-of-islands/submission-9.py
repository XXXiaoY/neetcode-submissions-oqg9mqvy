class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    q.append((i, j))
                    cnt += 1
                    while q:
                        r, c = q.pop()
                        for m, n in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            dr = r + m
                            dc = c + n
                            if dr in range(rows) and dc in range(cols) and grid[dr][dc] == '1':
                                q.append((dr,dc))
                                grid[dr][dc] = '0'
        
        return cnt
        