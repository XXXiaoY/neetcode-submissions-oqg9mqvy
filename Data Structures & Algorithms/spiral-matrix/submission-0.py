class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        ans = []

        while top <= bottom and left <= right:
            # 1. 走上边：从左到右
            for c in range(left, right + 1):
                ans.append(matrix[top][c])
            top += 1

            # 2. 走右边：从上到下
            for r in range(top, bottom + 1):
                ans.append(matrix[r][right])
            right -= 1

            # 3. 走下边：从右到左
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    ans.append(matrix[bottom][c])
                bottom -= 1

            # 4. 走左边：从下到上
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    ans.append(matrix[r][left])
                left += 1

        return ans