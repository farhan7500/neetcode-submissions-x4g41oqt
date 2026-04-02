class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count_map = {}
        for idx in range(len(nums)):
            difference = target - nums[idx]
            if target - nums[idx] in count_map:
                return [count_map[difference], idx]
            count_map[nums[idx]] = idx
        return None
        
        