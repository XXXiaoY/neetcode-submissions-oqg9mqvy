class MinStack:
    def __init__(self):
        self.stack = []      # 数据栈
        self.min_stack = []  # 辅助栈

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 如果最小栈为空，或者新值更小，则压入新值
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            # 否则，重复压入当前的最小值，保持高度同步
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]