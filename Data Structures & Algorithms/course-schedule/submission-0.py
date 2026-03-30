class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        count = [0] * numCourses
        graph = defaultdict(list)
        for pre, cur in prerequisites:
            graph[pre].append(cur)
            count[cur] += 1
        queue = deque()
        for i, val in enumerate(count):
            if val == 0:
                queue.append(i)
        studied = 0
        while queue:
            study = queue.popleft()
            studied += 1
            for courses in graph[study]:
                count[courses] -= 1
                if count[courses] == 0:
                    queue.append(courses)
        return studied == numCourses 

        

            
        