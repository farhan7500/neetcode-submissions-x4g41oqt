class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        left = right = 0
        char_map = {}

        while right < len(s):
            char_map[s[right]] = char_map.get(s[right], 0) + 1

            while (right - left + 1) - max(char_map.values()) > k:
                char_map[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

            right += 1
        return max_length

        