class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #{0:1}
        mp = defaultdict(list)
        pre_count = [0] * numCourses
        for c, pre in prerequisites:
            mp[pre].append(c)
            pre_count[c] += 1
        
        q = deque()
        
        for i, val in enumerate(pre_count):
            if val == 0:
                q.append(i)
        
        studied = 0
        while q:
            s = q.popleft()
            studied += 1
            for i in mp[s]:
                pre_count[i] -= 1
                if  pre_count[i] == 0:
                    q.append(i)
        
        return studied == numCourses




        