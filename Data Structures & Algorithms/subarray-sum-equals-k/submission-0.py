class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        s = 0
        mp[0] = 1
        cnt = 0

        for i in nums:
            s += i
            if s - k in mp:
                cnt += mp[s - k]
            mp[s] += 1
        
        return cnt
        