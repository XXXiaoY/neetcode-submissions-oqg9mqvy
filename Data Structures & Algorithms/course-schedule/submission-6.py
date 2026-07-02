from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        # Build directed graph
        # [a, b] means b -> a
        for a, b in prerequisites:
            graph[b].append(a)

        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        def dfs(course: int) -> bool:
            # If we see a node that is already in the current path,
            # we found a cycle.
            if state[course] == 1:
                return False

            # If this node has already been checked and is safe,
            # no need to check again.
            if state[course] == 2:
                return True

            # Mark as currently visiting
            state[course] = 1

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            # Mark as fully visited
            state[course] = 2
            return True

        # Need to check every course because the graph may be disconnected
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True