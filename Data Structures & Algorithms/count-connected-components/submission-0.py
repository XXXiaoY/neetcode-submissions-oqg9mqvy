class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        self.count = n # 初始时有 n 个独立分量
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
            
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootX] = rootY
                self.count -= 1 # 每次合并，分量减 1
        
        for u, v in edges:
            union(u, v)
            
        return self.count