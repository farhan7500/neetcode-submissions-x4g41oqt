class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = collections.Counter(nums)
        index = 0
        for _ in range(counter[0]):
            nums[index] = 0
            index += 1
        for _ in range(counter[1]):
            nums[index] = 1
            index += 1
        for _ in range(counter[2]):
            nums[index] = 2
            index += 1

        
        