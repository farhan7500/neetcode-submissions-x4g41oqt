class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set()
        for num in nums:
            num_set.add(num)

        max_count = 1
        for num in num_set:
            if num + 1 not in num_set:
                curr_max = 1
                while num - 1 in num_set:
                    curr_max += 1
                    max_count = max(curr_max, max_count)
                    num -= 1
        return max_count
        