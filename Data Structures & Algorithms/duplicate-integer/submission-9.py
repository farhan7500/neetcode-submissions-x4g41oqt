class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        target_set = set()
        for num in nums:
            if num in target_set:
                return True
            target_set.add(num)
        return False
        