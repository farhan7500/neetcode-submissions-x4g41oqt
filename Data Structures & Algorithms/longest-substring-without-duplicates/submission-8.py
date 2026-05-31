class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_count = 0
        char_set = set()

        # Iterate through each element
            # While dupicate exists, shrink from left
            # increment left
        # add right character
        # update max_count

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_count = max(max_count, right - left + 1)

        return max_count

