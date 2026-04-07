class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        if len(self.small) > len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0])/2
        else:
            return -self.small[0]
        
        