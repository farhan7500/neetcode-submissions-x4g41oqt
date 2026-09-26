class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]

        for idx in range(1, len(nums)):
            if curr_sum > 0:
                curr_sum += nums[idx]
            else:
                curr_sum = nums[idx]

            max_sum = max(max_sum, curr_sum)

        return max_sum
        