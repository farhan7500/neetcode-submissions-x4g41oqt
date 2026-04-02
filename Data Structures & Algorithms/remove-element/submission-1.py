class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0
        while pos < len(nums):
            if nums[pos] == val:
                nums.pop(pos)
            else:
                pos += 1
        return len(nums)
