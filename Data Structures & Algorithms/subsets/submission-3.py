class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        sol = []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return

            for choice in [True, False]:
                if choice:
                    sol.append(nums[i])

                backtrack(i + 1)

                if choice:
                    sol.pop()

        backtrack(0)
        return res