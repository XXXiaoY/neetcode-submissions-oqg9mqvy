class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        max_l = 0
        max_r = 0
        l = 0
        r = len(height) - 1
        while l < r:
            if height[l] < height[r]:
                if max_l < height[l]:
                    max_l = height[l]
                else:
                    water += max_l - height[l]
                l += 1
            else:
                if max_r < height[r]:
                    max_r = height[r]
                else:
                    water += max_r - height[r]
                r -= 1
        return water



        