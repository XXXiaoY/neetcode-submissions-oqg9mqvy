class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for i in stones:
            heapq.heappush(max_heap,-i)
        while len(max_heap) >= 2:
            max1 = -heapq.heappop(max_heap)
            max2 = -heapq.heappop(max_heap)
            minus = max1 - max2
            heapq.heappush(max_heap, -minus)
        return -max_heap[0]

  
        