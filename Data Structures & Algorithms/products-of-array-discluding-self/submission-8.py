class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        prefix_list = [prefix]
        for i in range(len(nums) - 1):
            prefix = prefix * nums[i]
            prefix_list.append(prefix)

        postfix = 1
        postfix_list = [postfix]
        for i in range(len(nums)-1, 0, -1):
            postfix = postfix * nums[i]
            postfix_list.insert(0, postfix)

        result = []

        for i in range(len(prefix_list)):
            result.append(prefix_list[i] * postfix_list[i])

        return result
        