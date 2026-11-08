class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        char_set = set()

        max_window = 0

        for right in range(len(s)):
            # Check for overflow
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the element
            char_set.add(s[right])

            max_window = max(max_window, right - left + 1)
        return max_window
        