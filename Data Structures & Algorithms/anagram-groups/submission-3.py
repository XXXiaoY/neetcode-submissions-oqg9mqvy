class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for i in strs:
            c = [0] * 26
            for char in i:
                c[ord(char) - ord('a')] += 1
            mp[tuple(c)].append(i)
        
        return list(mp.values())


        