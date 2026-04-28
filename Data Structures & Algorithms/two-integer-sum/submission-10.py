class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Maintain a map of key(difference): value(index)
        difference_map = {}

        # Iterate over the numbers, check is target - num is present
        # in the difference map. If yes, we get a hit and return the
        # index. Otherwise add to the difference map with current num
        # and current index
        for idx, num in enumerate(nums):
            difference = target - num
            if difference in difference_map:
                return [difference_map[difference], idx]
            difference_map[num] = idx