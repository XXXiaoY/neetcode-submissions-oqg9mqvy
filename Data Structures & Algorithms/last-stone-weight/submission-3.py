class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap,-i)
        
        while len(heap) > 1:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap)
            if s1 > s2:
                heapq.heappush(heap,(s2 - s1))
        
        return -heap[0] if heap else 0

        