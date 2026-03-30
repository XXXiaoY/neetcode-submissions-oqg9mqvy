class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        s = 0
        l_max = 0
        r_max = 0
        while left < right:
            if height[left] < height[right]:
                if l_max > height[left]:
                    s += l_max - height[left]                
                l_max = max(l_max,height[left])
                left += 1
            else:
                if r_max > height[right]:
                    s += r_max - height[right]
                r_max = max(r_max, height[right])
                right -= 1
        return s


        