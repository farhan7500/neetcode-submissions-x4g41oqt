class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_map = {}
        for num_num in range(len(nums)):
            difference = target - nums[num_num]
            if difference_map.get(difference) is not None:
                # Return the result here
                return [difference_map.get(difference), num_num]
            else:
                difference_map[nums[num_num]] = num_num