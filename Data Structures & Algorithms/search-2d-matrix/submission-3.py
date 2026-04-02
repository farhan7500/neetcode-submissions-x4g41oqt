class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        elements = []
        for row in matrix:
            elements += row

        left = 0
        right = len(elements) - 1
        while left <= right:
            mid = (left + right) // 2
            if elements[mid] == target:
                return True
            else:
                if elements[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        return False
        