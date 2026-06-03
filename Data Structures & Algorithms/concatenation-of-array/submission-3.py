class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result_list = [0] * 2 * size

        for idx in range(len(nums)):
            result_list[idx] = nums[idx]
            result_list[idx + size] = nums[idx]

        return result_list
