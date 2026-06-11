class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        mp = defaultdict(int)

        for i in nums:
            mp[i] += 1
        
        for i, val in mp.items():
            buckets[val].append(i)
        
        ans = []
        for i in range(len(buckets) - 1, -1, -1):
            for j in buckets[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans

        