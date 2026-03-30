class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i in nums:
            mp[i] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for v, c in mp.items():
            buckets[c].append(v)
        ans = []
        
        for j in range(len(nums), -1 , -1):
            for m in buckets[j]:
                if len(ans) < k:
                    ans.append(m)
                else:
                    break
        return ans
        