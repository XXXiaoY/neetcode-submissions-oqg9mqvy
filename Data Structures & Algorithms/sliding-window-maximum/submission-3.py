class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #method 1:max heap
        heap = []
        left = 0
        ans = []

        for right in range(len(nums)):
            val = nums[right]
            heapq.heappush(heap, (-val, right))
            if right - left + 1 == k:
                while heap[0][1] < left:
                    heapq.heappop(heap)
                ans.append(-heap[0][0])
                left += 1
        
        return ans
