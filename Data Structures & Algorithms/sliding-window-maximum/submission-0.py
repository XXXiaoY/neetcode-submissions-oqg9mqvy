class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque() # 存储索引，保持对应的值单调递减
        
        for i, n in enumerate(nums):
            # 1. 汰弱：如果新来的 n 比队尾的数大，队尾的就没用了
            while dq and nums[dq[-1]] < n:
                dq.pop()
            
            dq.append(i)
            
            # 2. 去旧：如果队首的索引已经滑出窗口了
            if dq[0] == i - k:
                dq.popleft()
            
            # 3. 记录答案：窗口长度达到 k 时开始记录
            if i >= k - 1:
                res.append(nums[dq[0]])
                
        return res


            
            