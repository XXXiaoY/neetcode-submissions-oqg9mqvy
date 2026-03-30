class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i in nums:
            mp[i] += 1
        ans = []
        s_mp = sorted(mp.items(), key=lambda x:x[1] , reverse=True)
        for num, freq in s_mp:
            if len(ans) < k:
                ans.append(num)
            else:
                break
        return ans