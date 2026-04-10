class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0
                    cnt = 0
                    

                    while q:
                        r, c = q.popleft()
                        cnt += 1
                        
                        for m, n in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                            dr = r + m
                            dc = c + n

                            if dr in range(rows) and dc in range(cols) and grid[dr][dc] == 1:
                                grid[dr][dc] = 0
                                q.append((dr, dc))
                    max_area = max(max_area, cnt)
        
        return max_area



        