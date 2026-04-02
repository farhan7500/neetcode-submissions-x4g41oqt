class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_map = {}
        for idx, num in enumerate(nums):
            difference = target - num
            if difference in difference_map:
                if idx < difference_map[difference]:
                    return [idx, difference_map[difference]]
                return [difference_map[difference], idx]
            else:
                difference_map[num] = idx
        
        