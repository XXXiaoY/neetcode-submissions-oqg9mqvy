class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else: # 遇到 '*'
                low -= 1
                high += 1
            
            # 如果最多可能的左括号都小于 0，说明右括号太多了
            if high < 0:
                return False
            
            # 最少可能的左括号不能小于 0（因为左括号数不能为负）
            low = max(low, 0)
            
        # 最后看最少剩下的左括号是否能为 0
        return low == 0
        