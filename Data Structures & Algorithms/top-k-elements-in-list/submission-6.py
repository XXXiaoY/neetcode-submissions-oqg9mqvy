class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i in nums:
            mp[i] += 1
        buckets = [[] for _ in range(len(nums) + 1)]

        for val, cnt in mp.items():
            buckets[cnt].append(val)
        ans = []
        for i in range(len(buckets) - 1, -1, -1):
            for j in buckets[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans

        