class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set()
        for num in nums:
            num_set.add(num)

        max_count = 1
        curr = 1
        for element in num_set:
            while element - 1 in num_set:
                curr += 1
                max_count = max(max_count, curr)
                element -= 1
            curr = 1
        return max_count
        