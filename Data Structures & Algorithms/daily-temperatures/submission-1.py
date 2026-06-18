class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                index, _ = stack.pop()
                ans[index] = i - index
            stack.append((i, val))
        
        return ans
        