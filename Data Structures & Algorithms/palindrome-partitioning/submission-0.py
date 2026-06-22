class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def is_palindrome(sub):
            l, r = 0, len(sub) - 1
            while l < r:
                if sub[l] != sub[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(start):
            if start == len(s):
                ans.append(path.copy())
                return

            for end in range(start, len(s)):
                sub = s[start:end + 1]

                if not is_palindrome(sub):
                    continue

                path.append(sub)
                dfs(end + 1)
                path.pop()

        dfs(0)
        return ans
    
    
        