class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        candidate = 1
        num_set = set(nums)
        while candidate in num_set:
            candidate += 1
        return candidate
        