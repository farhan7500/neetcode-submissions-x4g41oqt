class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Condition:
        # size of window - max_repeating <= k

        left = 0
        max_result = 0
        #current_result = 0

        count_map = {}

        for right in range(len(s)):
            count_map[s[right]] = count_map.get(s[right], 0) + 1
            window_size = right - left + 1
            max_key, max_val = self.get_max_kv(count_map)
            if window_size - max_val <= k:
                #current_result += 1
                max_result = max(max_result, window_size)
            else:
                count_map[s[left]] -= 1
                left += 1
                #current_result = 0
        return max_result


    def get_max_kv(self, count_map):
        max_key = max(count_map, key=count_map.get)
        max_val = count_map[max_key]
        return max_key, max_val
