class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        i = 0
        j = (rows * columns) - 1

        while i <= j:
            mid = (i + j) // 2
            mid_val = matrix[mid // columns][mid % columns]
            if mid_val == target:
                return True
            if mid_val > target:
                j = mid - 1
            else:
                i = mid + 1
            
        return False
