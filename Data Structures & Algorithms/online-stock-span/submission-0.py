class StockSpanner:
    # 栈底到栈顶，价格严格递减

    def __init__(self):
        self.stack = []  # each element is (price, span)

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            old_price, old_span = self.stack.pop()
            span += old_span

        self.stack.append((price, span))
        return span