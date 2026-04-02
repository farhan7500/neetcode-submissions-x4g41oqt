class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        total = 1
        for idx in range(len(nums) - 1):
            total *= nums[idx]
            pre.append(total)

        post = [1]
        total = 1
        for idx in range(len(nums) -1, 0, -1):
            total *= nums[idx]
            post.insert(0, total)

        result = []
        for idx in range(len(pre)):
            result.append(pre[idx] * post[idx])
        return result
