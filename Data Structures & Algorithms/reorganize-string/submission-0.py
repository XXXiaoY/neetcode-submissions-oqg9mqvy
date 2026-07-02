class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        n = len(s)

        # 如果最高频字符太多，不可能重排
        if max(count.values()) > (n + 1) // 2:
            return ""

        # Python heapq 是 min heap，所以用负数模拟 max heap
        heap = []
        for ch, freq in count.items():
            heapq.heappush(heap, (-freq, ch))

        res = []

        while len(heap) >= 2:
            freq1, ch1 = heapq.heappop(heap)
            freq2, ch2 = heapq.heappop(heap)

            res.append(ch1)
            res.append(ch2)

            # 因为 freq 是负数，所以 +1 表示使用掉一个
            freq1 += 1
            freq2 += 1

            if freq1 < 0:
                heapq.heappush(heap, (freq1, ch1))
            if freq2 < 0:
                heapq.heappush(heap, (freq2, ch2))

        # 如果还剩一个字符，直接加到最后
        if heap:
            freq, ch = heapq.heappop(heap)
            res.append(ch)

        return "".join(res)
        