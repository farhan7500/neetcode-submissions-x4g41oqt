class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        count_map = {}
        left = 0
        for right in range(len(s)):
            try:
                count_map[s[right]] += 1
            except KeyError:
                count_map[s[right]] = 1
        
            while (right - left + 1) - max(count_map.values()) > k:
                count_map[s[left]] -= 1
                left += 1
            
            result = max(right - left + 1, result)
        return result
        