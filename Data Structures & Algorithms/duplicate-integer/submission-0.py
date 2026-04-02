class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_map = {}
        for num in nums:
            try:
                num_map[num]
                return True
            except KeyError:
                num_map[num] = 1
        return False
         