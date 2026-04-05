class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = defaultdict(list)
        c_need = defaultdict(int)
        for c, pre in prerequisites:
            mp[pre].append(c)
            c_need[c] += 1
        q = deque()
        
        for i in range(numCourses):     # 遍历所有课程
            if c_need[i] == 0:          # 没有前置要求的
                q.append(i)
        
        studied = 0
        while q:
            cur = q.popleft()
            studied += 1
            for i in mp[cur]:
                c_need[i] -= 1
                if c_need[i] == 0:
                    q.append(i)
        
        return True if studied == numCourses else False

        