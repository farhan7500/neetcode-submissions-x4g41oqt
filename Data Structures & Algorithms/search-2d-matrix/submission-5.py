class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] >= target:
                # Now we know this the row to target
                return self.bsearch(row, target)
        return False

    def bsearch(self, clist, target):
        i = 0
        j = len(clist) - 1
        while i <= j:
            mid = (i + j) // 2
            if clist[mid] == target:
                return True
            elif clist[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return False
