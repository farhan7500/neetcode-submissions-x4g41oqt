class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a diff_map {difference: idx}
        diff_map = {}

        # Iterate over the list
            # If (target - num) in diff_set
                # return indices
            # add num to diff_set
        for idx in range(len(nums)):
            if target - nums[idx] in diff_map:
                return [diff_map[target - nums[idx]], idx]
            diff_map[nums[idx]] = idx
        return []
        