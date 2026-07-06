class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = defaultdict(list)

        for i in strs:
            char = [0] * 26
            for j in i:
                char[ord(j) - ord('a')] += 1
            mp[tuple(char)].append(i)
        
        return list(mp.values())

        