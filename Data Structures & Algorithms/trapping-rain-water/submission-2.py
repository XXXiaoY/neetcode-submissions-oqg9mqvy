class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        l_max = 0
        r_max = 0
        water = 0
        while left < right:
            if height[left] > height[right]:
                if height[right] < r_max:
                    water += r_max -  height[right]
                r_max = max(r_max, height[right])
                right -= 1
            else:
                if height[left] < l_max:
                    water += l_max - height[left]
                l_max = max(l_max, height[left])
                left += 1
        
        return water

        