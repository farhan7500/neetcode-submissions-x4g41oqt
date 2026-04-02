class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        maximum = 0
        left = 0
        right = 0
        while right < len(s):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            maximum = max(right - left + 1, maximum)
            right += 1
        return maximum
    
        