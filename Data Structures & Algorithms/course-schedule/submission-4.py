class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = defaultdict(list)
        need = [0] * numCourses

        for c, pre in prerequisites:
            mp[pre].append(c)
            need[c] += 1
        
        q = deque()
        
        for index, i in enumerate(need):
            if i == 0:
                q.append(index)
        
        studied = 0
        while q:
            c = q.pop()
            studied += 1
            for j in mp[c]:
                need[j] -= 1
                if need[j] == 0:
                    q.append(j)

        

        


        return studied == numCourses

        