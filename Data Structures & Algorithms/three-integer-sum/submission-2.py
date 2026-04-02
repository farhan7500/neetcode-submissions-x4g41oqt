class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for idx in range(len(nums)):
            numbers = nums[idx + 1:]
            result = self.twoSum(nums[idx], numbers, 0 - nums[idx])
            for r in result:
                if r not in res:
                    res.append(r)
        return res

    def twoSum(self, number, numbers, target):
        i = 0
        j = len(numbers) - 1
        result_list = []
        while i < j:
            target_sum = numbers[i] + numbers[j]
            if target_sum == target:
                result_list.append([number, numbers[i], numbers[j]])
            if target_sum > target:
                j -= 1
            else:
                i += 1
        return result_list

        