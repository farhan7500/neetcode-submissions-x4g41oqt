class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        char_map = {}
        max_size = 0

        for right in range(len(s)):
            char_map[s[right]] = char_map.get(s[right], 0) + 1

            max_val = max(char_map.values())

            while right - left + 1 - max_val > k:
                char_map[s[left]] -= 1
                left += 1
                
            max_size = max(max_size, right - left + 1)
            
        return max_size

        