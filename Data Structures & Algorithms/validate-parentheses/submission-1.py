class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'}': '{', ')': '(', ']': '['}
        stack = []

        for i in s:
            if i in mp:
                if stack:
                    top = stack.pop()
                    if top != mp[i]:
                        return False
                else:
                    return False
            else:
                stack.append(i)
            
        return not stack
        