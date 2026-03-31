class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        q = deque()
        time = 0

        for i in range(rows):
            for j in range(cols):
                cur = grid[i][j]
                if cur == 1:
                    fresh += 1
                elif cur == 2:
                    q.append([i,j])

        if fresh == 0: return 0
        
        while q and fresh > 0:
            time += 1

            for _ in range(len(q)):
                r, c = q.popleft()
                for m, n in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    rd = r + m
                    nd = c + n
                    if rd in range(rows) and nd in range(cols) and grid[rd][nd] == 1:
                        q.append([rd, nd])
                        grid[rd][nd] = 2
                        fresh -= 1

        return time if fresh == 0 else - 1    
           
   



        