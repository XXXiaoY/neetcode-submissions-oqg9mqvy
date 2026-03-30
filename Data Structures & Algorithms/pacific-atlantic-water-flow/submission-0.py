class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        
        m, n = len(heights), len(heights[0])
        # 两个标记本：记录海水能否倒灌到这里
        can_reach_p = [[False] * n for _ in range(m)]
        can_reach_a = [[False] * n for _ in range(m)]

        def dfs(r, c, reachable):
            reachable[r][c] = True
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                # 倒灌条件：1. 不越界 2. 没访问过 3. 目标高度 >= 当前高度 (水往高处走)
                if (0 <= nr < m and 0 <= nc < n and 
                    not reachable[nr][nc] and 
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable)

        # 1. 从左右边界开始“倒灌”
        for i in range(m):
            dfs(i, 0, can_reach_p)      # 左边：太平洋
            dfs(i, n - 1, can_reach_a)  # 右边：大西洋

        # 2. 从上下边界开始“倒灌”
        for j in range(n):
            dfs(0, j, can_reach_p)      # 上边：太平洋
            dfs(m - 1, j, can_reach_a)  # 下边：大西洋

        # 3. 找交集：两个本子都打钩的坐标
        ans = []
        for i in range(m):
            for j in range(n):
                if can_reach_p[i][j] and can_reach_a[i][j]:
                    ans.append([i, j])
        return ans