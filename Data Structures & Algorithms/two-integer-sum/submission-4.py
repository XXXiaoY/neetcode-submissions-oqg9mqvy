class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = defaultdict(int)

        for i, val in enumerate(nums):
            if target - val in mp:
                return [mp[target - val], i]
            mp[val] = i
        