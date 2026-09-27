class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = None
        curr_sum = 0

        left = right = 0

        while right < len(nums):
            curr_sum += nums[right]
            while curr_sum >= target:
                if min_size is None:
                    min_size = right - left + 1
                else:
                    min_size = min(min_size, right - left + 1)

                if min_size == 1:
                    return 1

                curr_sum -= nums[left]
                left += 1
            right += 1

        if min_size is None:
            return 0
        return min_size
