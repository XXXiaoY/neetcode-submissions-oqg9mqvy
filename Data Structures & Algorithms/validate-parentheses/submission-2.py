class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', '}':'{', ']':'['}
        stack = []

        for i in s:
            if i in dic:
                if stack:
                    if stack[-1] != dic[i]:
                        return False
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(i)
        
        return True if not stack else False
                    
        