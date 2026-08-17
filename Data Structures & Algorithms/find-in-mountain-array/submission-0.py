# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l = 0
        r = length - 1
        while l < r:
            mid = (l + r) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l

        if mountainArr.get(peak) == target:
            return peak
        
        l = 0
        r = peak - 1
        while l < r:
            mid = (l + r) // 2
            if mountainArr.get(mid) >= target:
                r = mid 
            else:
                l = mid + 1
        if mountainArr.get(l) == target:
            return l
        
        l = peak + 1
        r = length - 1
        while l < r:
            mid = (l + r) // 2
            if mountainArr.get(mid) <= target:
                r = mid 
            else:
                l = mid + 1
        if mountainArr.get(l) == target:
            return l
        return -1

        