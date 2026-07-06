from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check if first row should be zero
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_zero = True
                break

        # Check if first column should be zero
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True
                break

        # Use first row and first column as markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Set cells to zero based on markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Zero out first row if needed
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0

        # Zero out first column if needed
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0