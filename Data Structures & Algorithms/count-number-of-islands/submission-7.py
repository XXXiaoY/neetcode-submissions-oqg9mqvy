class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    q.append([i, j])
                    grid[i][j] == '0'

                    while q:
                        r, c = q.pop()
                        for m, n in [(1, 0), (-1, 0),(0, 1), (0, -1)]:
                            dr = r + m
                            dc = c + n

                            if dr in range(rows) and dc in range(cols) and grid[dr][dc] == '1':
                                grid[dr][dc] = '0'
                                q.append([dr, dc])
        
        return count
        