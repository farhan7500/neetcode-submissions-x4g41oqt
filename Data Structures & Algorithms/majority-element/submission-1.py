class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            try:
                count_dict[num] += 1
                if count_dict[num] > len(nums) // 2:
                    return num
            except KeyError:
                count_dict[num] = 1