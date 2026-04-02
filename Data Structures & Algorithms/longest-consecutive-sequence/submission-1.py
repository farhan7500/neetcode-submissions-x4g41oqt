class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        element_map = {}
        for num in nums:
            element_map[num] = 1

        max_count = 1
        current_count = 1
        for element in element_map:
            test_element = element
            while (test_element - 1) in element_map:
                current_count += 1
                max_count = max(max_count, current_count)
                test_element -= 1
            current_count = 1

        return max_count



        