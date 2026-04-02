class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for idx in range(len(nums)):
            difference = target - nums[idx]
            if difference in diff_map:
                return [diff_map[difference], idx]
            diff_map[nums[idx]] = idx
        return null

        