class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_s = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    a = 1
                    q = deque([(i, j)])
                    grid[i][j] = 0
                    while q:
                        r, c = q.popleft()
                        for m, n in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            rd = r + m
                            cd = c + n
                            if rd in range(rows) and cd in range(cols) and grid[rd][cd] == 1:
                                a += 1
                                grid[rd][cd] = 0
                                q.append((rd,cd))
                    max_s = max(max_s, a)
        return max_s
                        


        