class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' :
                    count += 1
                    grid[i][j] = '0'
                    q.append((i, j))

                    while q:
                        r, c = q.popleft()
                        for m, n in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            rd = r + m
                            cd = c + n
                            if rd in range(rows) and cd in range(cols) and grid[rd][cd] == '1':
                                grid[rd][cd] = '0'
                                q.append((rd,cd))
                        
        
        return count

        