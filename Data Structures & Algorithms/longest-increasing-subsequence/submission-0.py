class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:

            pos = self.binary_search(tails, num)

            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num

        return len(tails)

    def binary_search(self, arr, target):

        left = 0
        right = len(arr)

        while left < right:

            mid = (left + right) // 2

            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left
        