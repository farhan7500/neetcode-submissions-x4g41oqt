class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_size = 0
        count_map = {}
        
        for right in range(len(s)):
            count_map[s[right]] = count_map.get(s[right], 0) + 1
            max_val = max(count_map.values())
            if (right - left + 1) - max_val > k:
                count_map[s[left]] -= 1
                left += 1
            else:
                max_size = max(max_size, right - left + 1)
        return max_size
        
