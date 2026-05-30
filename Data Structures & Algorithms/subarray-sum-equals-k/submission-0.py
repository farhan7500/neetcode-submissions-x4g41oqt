class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        curr_prefix_sum = 0
        prefix_sum_map = {0: 1}

        for num in nums:
            curr_prefix_sum += num

            if (curr_prefix_sum - k) in prefix_sum_map:
                result += prefix_sum_map[curr_prefix_sum - k]
            prefix_sum_map[curr_prefix_sum] = prefix_sum_map.get(curr_prefix_sum, 0) + 1
        return result