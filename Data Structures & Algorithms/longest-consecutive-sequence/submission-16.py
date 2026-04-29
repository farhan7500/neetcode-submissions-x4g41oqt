class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        num_set = set()
        for num in nums:
            num_set.add(num)

        overall_max = 0
        for num in num_set:
            if num + 1 not in num_set:
                curr_max = 0
                while (num - 1) in num_set:
                    curr_max += 1
                    overall_max = max(overall_max, curr_max)
                    num = num - 1

        return overall_max + 1