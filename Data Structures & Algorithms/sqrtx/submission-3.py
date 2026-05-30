class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        res = 0

        while left <= right:
            mid = left + ((right -left) // 2)
            mid_squared = mid * mid
            if x == mid_squared:
                return mid
            if x > mid_squared:
                left = mid + 1
                res = mid
            else:
                right = mid - 1
        return res
