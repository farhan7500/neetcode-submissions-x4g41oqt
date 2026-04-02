class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_to_search = -1
        for row in matrix:
            if row[0] <= target <= row[-1]:
                row_to_search = row
                break

        if row_to_search == -1:
            return False

        if self.b_search(row_to_search, target) is not None:
            return True
        return False


    def b_search(self, nums, num):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == num:
                return mid
            if nums[mid] >= num:
                right = mid - 1
            else:
                left = mid + 1
        return None
        