from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        heap = []
        for task, freq in count.items():
            heapq.heappush(heap, (-freq, task))

        cooldown = deque()  # (ready_time, remaining_freq, task)

        time = 0

        while heap or cooldown:
            # 1. 把冷却结束的任务放回 heap
            while cooldown and cooldown[0][0] <= time:
                ready_time, freq, task = cooldown.popleft()
                heapq.heappush(heap, (freq, task))

            # 2. 执行当前剩余次数最多的任务
            if heap:
                freq, task = heapq.heappop(heap)
                freq += 1  # 因为 freq 是负数，+1 表示少执行了一次

                # 3. 如果这个任务还没做完，放进冷却队列
                if freq != 0:
                    cooldown.append((time + n + 1, freq, task))

            # 无论执行任务还是 idle，时间都要过 1
            time += 1

        return time