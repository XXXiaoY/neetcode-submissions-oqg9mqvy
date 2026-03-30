class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = defaultdict(int)
        for i, val in enumerate(nums):
            if (target - val) in s:
                return[s[target-val],i]
            else:
                s[val] = i
        
