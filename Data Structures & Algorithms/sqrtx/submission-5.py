class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        res = 0

        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid

            if mid_squared == x:
                return mid
            if mid_squared > x:
                right = mid - 1
            else:
                left = mid + 1
                res = mid

        return res
        