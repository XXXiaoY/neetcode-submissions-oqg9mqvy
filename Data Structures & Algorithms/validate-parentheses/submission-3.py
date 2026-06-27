class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')': '(', '}': '{', ']': '['}
        stack = []

        for i in s:
            if i in mp:
                if not stack or stack[-1] != mp[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        
        return False if stack else True
        