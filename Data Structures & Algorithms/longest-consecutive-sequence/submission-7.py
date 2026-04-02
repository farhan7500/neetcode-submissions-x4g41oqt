class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sequence = 0
        current_sequence = 0
        nums_map = {}
        for num in nums:
            nums_map[num] = 1

        for item in nums_map:
            current_sequence += 1
            while item - 1 in nums_map:
                current_sequence += 1
                item -= 1

            max_sequence = max(max_sequence, current_sequence)
            current_sequence = 0

        return max_sequence
        