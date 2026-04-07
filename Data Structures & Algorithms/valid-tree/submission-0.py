class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 即使这里不写 len(edges) != n - 1，下面的逻辑依然严谨
        
        par = [i for i in range(n)]
        # 初始有 n 个点，每个点都是一个独立的连通分量
        self.count = n 

        def find(i):
            if par[i] != i:
                par[i] = find(par[i])
            return par[i]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False # 【条件 1 失败】：发现环，不是树
            
            par[p1] = p2
            self.count -= 1 # 每次成功合并，连通分量减 1
            return True
        
        for u, v in edges:
            if not union(u, v):
                return False # 只要有环，立即返回 False
        
        # 【条件 2 检查】：最后必须所有的点都连在一起，形成唯一的一个大岛
        return self.count == 1