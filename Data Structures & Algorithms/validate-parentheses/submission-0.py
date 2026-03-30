class Solution:
    def isValid(self, s: str) -> bool:
        map = {'}':'{', ']':'[', ')':'('}
        stack = []
        for i in s:
            if i in map:
                if not stack or stack.pop() != map[i]:
                    return False
            
            else:
                stack.append(i)
        
        return not stack

        