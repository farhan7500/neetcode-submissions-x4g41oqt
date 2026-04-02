class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_map = {}
        for idx, num in enumerate(nums):
            difference = target - num
            if difference in difference_map:
                return [difference_map[difference], idx]
            difference_map[num] = idx
        return []
