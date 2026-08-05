class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        left = 0
        right = (rows * columns) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_val = matrix[mid // columns][mid % columns]
            if mid_val == target:
                return True
            if mid_val > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
        