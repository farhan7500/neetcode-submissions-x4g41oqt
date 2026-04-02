class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        continue_execution = True
        while continue_execution:
            try:
                nums.remove(val)
            except ValueError:
                continue_execution = False
        return len(nums)
