class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        candidate = 1
        # nums_set = set(nums)
        while candidate in nums:
            candidate += 1
        return candidate
        