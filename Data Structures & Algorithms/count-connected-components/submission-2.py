class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connect = defaultdict(list)
        for i, j in edges:
            connect[i].append(j)
            connect[j].append(i)
        
        cnt = 0
        visited = set()
        def dfs(cur):
            if cur in visited:
                return
            visited.add(cur)
            for i in connect[cur]:
                dfs(i)

        for i in range(n):
            if i not in visited:
                cnt += 1
                dfs(i)
        
        return cnt

        

        