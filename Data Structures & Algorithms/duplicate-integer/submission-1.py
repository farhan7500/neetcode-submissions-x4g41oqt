class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        item_map = {}
        for item in nums:
            try:
                item_map[item]
                return True
            except KeyError:
                item_map[item] = 1
        return False
         