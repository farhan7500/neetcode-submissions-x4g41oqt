class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        prefix = [pre]
        for idx in range(len(nums) - 1):
            pre = pre * nums[idx]
            prefix.append(pre)

        post = 1
        postfix = [post]
        for idx in range(len(nums) - 1, 0, -1):
            post = post * nums[idx]
            postfix.insert(0, post)

        result = []
        for idx in range(len(nums)):
            result.append(prefix[idx] * postfix[idx])

        return result

        