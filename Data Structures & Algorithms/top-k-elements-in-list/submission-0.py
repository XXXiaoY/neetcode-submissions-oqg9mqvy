class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_nums = {}
        for i in nums:
            c_nums[i] = 1 + c_nums.get(i, 0)
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, cnt in c_nums.items():
            buckets[cnt].append(key)
        
        res = []

        for i in range(len(buckets) - 1, 0, -1):
            for val in buckets[i]:
                res.append(val)
                if len(res) == k:
                    return res


            
        