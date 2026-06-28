class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        need = defaultdict(list)
        remain = [0] * numCourses

        for c, p in prerequisites:
            need[p].append(c)
            remain[c] += 1
        
        q = deque()
        for i, val in enumerate(remain):
            if val == 0:
                q.append(i)
        
        studied = 0
        while q:
            cur = q.popleft()
            studied += 1
            for m in need[cur]:
                remain[m] -= 1
                if remain[m] == 0:
                    q.append(m)
        
        return True if studied == numCourses else False

        