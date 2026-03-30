class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        mp = defaultdict(list)
        for i in strs:
            count_char = [0] * 26
            for j in i:
                count_char[ord(j) - ord('a')] += 1
            mp[tuple(count_char)].append(i)
        return list(mp.values())
        

        