class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i in nums:
            mp[i] += 1
        buckets = [[] for _ in range(len(nums) + 1)] 
        for val, cnt in mp.items():
            buckets[cnt].append(val)
        ans = []
        for m in range(len(nums), -1, -1):
            if buckets[m]:
                for v in buckets[m]:
                    if len(ans) < k:
                        ans.append(v)
                    else:
                        break
        return ans
    
    


                    