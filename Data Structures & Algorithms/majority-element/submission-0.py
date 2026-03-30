class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        for x in nums:
            mp[x] += 1
        return max(mp, key=mp.get)
        