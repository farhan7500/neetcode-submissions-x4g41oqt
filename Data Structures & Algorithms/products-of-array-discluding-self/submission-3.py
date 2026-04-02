class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        pre_result_list = [1]
        for idx in range(len(nums) - 1):
            pre *= nums[idx]
            pre_result_list.append(pre)

        post = 1
        post_result_list = [1]

        for idx in range(len(nums) - 1, 0, -1):
            post *= nums[idx]
            post_result_list.insert(0, post)

        result_list = []
        for idx in range(len(pre_result_list)):
            result_list.append(pre_result_list[idx] * post_result_list[idx])

        return result_list

        