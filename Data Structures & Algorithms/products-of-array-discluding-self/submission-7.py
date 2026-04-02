class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_list = [1]
        prefix = 1
        for idx in range(len(nums) - 1):
            prefix = prefix * nums[idx]
            prefix_list.append(prefix)

        postfix_list = [1]
        postfix = 1
        for idx in range(len(nums) - 1, 0, -1):
            postfix = postfix * nums[idx]
            postfix_list.insert(0, postfix)

        result = []
        for i in range(len(nums)):
            result.append(prefix_list[i] * postfix_list[i])

        return result