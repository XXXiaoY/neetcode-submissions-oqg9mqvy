class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        visited = set()

        count = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i, j) not in visited:
                    visited.add((i, j))
                    count += 1
                    q = deque([(i, j)])
                    while q:
                        m ,n = q.popleft()
                        for r ,c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            cur_row = m + r
                            cur_col = n + c

                            if 0 <= cur_row < row and 0 <= cur_col < col and \
                               grid[cur_row][cur_col] == '1' and \
                               (cur_row, cur_col) not in visited:
                                
                                visited.add((cur_row, cur_col))
                                q.append((cur_row, cur_col))

        return count





        