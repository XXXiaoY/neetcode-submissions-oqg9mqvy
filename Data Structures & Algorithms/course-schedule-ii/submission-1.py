class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = [0] * numCourses
        need = defaultdict(list)

        for cur, pre in prerequisites:
            need[pre].append(cur)
            mp[cur] += 1
        q = deque()
        
        for i, val in enumerate(mp):
            if val == 0:
                q.append(i)
        ans = []
        
        while q:
            c = q.popleft()
            ans.append(c)
            numCourses -= 1
            for can in need[c]:
                mp[can] -= 1
                if mp[can] == 0:
                    q.append(can)
        
        return ans if numCourses == 0 else[]


        