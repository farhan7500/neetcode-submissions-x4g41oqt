class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_size = len(nums) + 1
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_size = min(min_size, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        if min_size == len(nums) + 1:
            return 0
        return min_size



        
        