class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = collections.Counter(nums)
        index = 0
        if counter.get(0) is not None:
            for _ in range(counter[0]):
                nums[index] = 0
                index += 1
        if counter.get(1) is not None:
            for _ in range(counter[1]):
                nums[index] = 1
                index += 1
        if counter.get(2) is not None:
            for _ in range(counter[2]):
                nums[index] = 2
                index += 1

        
        