class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_size = 0
        count_map = {}

        for right in range(len(s)):
            count_map[s[right]] = count_map.get(s[right], 0) + 1
            window_size = right - left + 1
            max_val = max(count_map.values())
            if window_size - max_val <= k:
                max_size = max(max_size, window_size)
            else:
                count_map[s[left]] -= 1
                left += 1
        return max_size
        
