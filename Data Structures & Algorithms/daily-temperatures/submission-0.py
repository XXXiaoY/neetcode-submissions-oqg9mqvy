class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                top, insert = stack.pop()
                ans[insert] = i - insert
            stack.append((val, i))
        
        return ans
                
 
        