class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        character_set = set()
        for num in nums:
            if num in character_set:
                return True
            else:
                character_set.add(num)
        return False
         