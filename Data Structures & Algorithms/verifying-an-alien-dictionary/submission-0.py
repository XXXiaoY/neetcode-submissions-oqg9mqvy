class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {c: i for i, c in enumerate(order)}

        def in_order(w1: str, w2: str) -> bool:
            m, n = len(w1), len(w2)
            i = 0

            while i < m and i < n:
                if w1[i] != w2[i]:
                    return rank[w1[i]] < rank[w2[i]]
                i += 1

            return m <= n

        for i in range(len(words) - 1):
            if not in_order(words[i], words[i + 1]):
                return False
        return True
        