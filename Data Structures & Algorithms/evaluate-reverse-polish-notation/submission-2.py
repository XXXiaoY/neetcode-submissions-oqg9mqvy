class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        s = {'+', '-', '*', "/"}
        for i in tokens:
            if i not in s:
                stack.append(i)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if i == '-':
                    stack.append(b - a)
                if i == '+':
                    stack.append(b + a)
                if i == '*':
                    stack.append(b * a)
                if i == '/':
                    stack.append(b / a)
        
        return int(stack[-1])

        