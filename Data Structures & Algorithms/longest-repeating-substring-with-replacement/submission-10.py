class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Write your code here
        max_result = 0
        max_char = 0
        char_map = {}
        left = right = 0
        while right < len(s):
            char_map[s[right]] = char_map.get(s[right], 0) + 1
            max_char = max(max_char, char_map[s[right]])

            while right - left + 1 - max_char > k:
                char_map[s[left]] -= 1
                left += 1
            
            max_result = max(max_result, right - left + 1)
            right += 1

        return max_result

        