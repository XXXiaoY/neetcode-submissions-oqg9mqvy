class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s_count = Counter(s1)
        mp = defaultdict(int)
        left = 0
        for right in range(len(s2)):
            val = s2[right]
            mp[val] += 1
            if right - left + 1 > len(s1):
                mp[s2[left]] -= 1
                if mp[s2[left]] == 0:
                    del mp[s2[left]]
                left += 1
            if s_count == mp:
                return True
        return False

        