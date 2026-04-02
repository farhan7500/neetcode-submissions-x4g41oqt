class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            num_set.add(num)
        longest = 0
        for num in nums:
            current_longest = 0
            while num in num_set:
                current_longest += 1
                longest = max(longest, current_longest)
                num = num - 1
        return longest
   
        