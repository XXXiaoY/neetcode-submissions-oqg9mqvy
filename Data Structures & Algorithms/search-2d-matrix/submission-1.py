class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n  # 搜索范围 [0, m*n)
        
        while left < right:
            mid = (left + right) // 2
            
            # 关键：一维索引转二维坐标
            row = mid // n
            col = mid % n
            num = matrix[row][col]
            
            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid
                
        return False