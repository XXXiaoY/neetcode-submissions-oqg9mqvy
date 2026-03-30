from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque() # 存储索引，对应的值单调递减
        
        for i in range(len(nums)):
            # 1. 保持单调递减：踢走所有比当前值小的队尾元素
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            
            q.append(i)
            
            # 2. 移除过期的左侧索引
            if q[0] <= i - k:
                q.popleft()
            
            # 3. 窗口形成后开始记录
            if i >= k - 1:
                ans.append(nums[q[0]])
                
        return ans