class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        right = m*n - 1
        left = 0
        while left <= right:
            mid = (right + left) // 2
            row = mid // n
            col = mid % n
            pivot_value = matrix[row][col]
            if pivot_value == target:
                return True
            elif pivot_value < target:
                left = mid + 1
            elif pivot_value > target: 
                right = mid - 1
        return False
        