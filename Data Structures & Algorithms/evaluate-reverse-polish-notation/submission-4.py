class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        s = {'+', '-', '*', "/"}
        for i in tokens:
            if i not in s:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == '-':
                    stack.append(b - a)
                if i == '+':
                    stack.append(b + a)
                if i == '*':
                    stack.append(b * a)
                if i == '/':
                    stack.append(int(b / a))
        
        return int(stack[-1])

        