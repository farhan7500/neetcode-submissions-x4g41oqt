class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        prefix_list = [1]
        for idx in range(len(nums) - 1):
            prefix = prefix * nums[idx]
            prefix_list.append(prefix)

        postfix = 1
        postfix_list = [1]
        for idx in range(len(nums) - 1, 0, -1):
            postfix = postfix * nums[idx]
            postfix_list.insert(0, postfix)

        result_list = []
        for idx in range(len(nums)):
            result_list.append(prefix_list[idx] * postfix_list[idx])
        return result_list

        