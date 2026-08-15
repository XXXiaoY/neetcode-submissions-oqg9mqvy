class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r1: int, c1: int, r2: int, c2: int) -> 'Node':
            # 检查当前区域 [r1..r2, c1..c2] 的元素是否全部相同
            is_same = True
            val = grid[r1][c1]
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if grid[i][j] != val:
                        is_same = False
                        break
                if not is_same:
                    break
            
            # 全相同，直接返回叶子节点
            if is_same:
                return Node(val == 1, True, None, None, None, None)
            
            # 不相同，划分为 4 个子区域递归处理
            mid_r = (r1 + r2) // 2
            mid_c = (c1 + c2) // 2
            
            top_left = dfs(r1, c1, mid_r, mid_c)
            top_right = dfs(r1, mid_c + 1, mid_r, c2)
            bottom_left = dfs(mid_r + 1, c1, r2, mid_c)
            bottom_right = dfs(mid_r + 1, mid_c + 1, r2, c2)
            
            return Node(True, False, top_left, top_right, bottom_left, bottom_right)
            
        n = len(grid)
        return dfs(0, 0, n - 1, n - 1)