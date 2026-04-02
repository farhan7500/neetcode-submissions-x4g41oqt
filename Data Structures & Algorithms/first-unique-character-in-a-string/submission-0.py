class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = {}
        for character in s:
            try:
                char_map[character] += 1
            except KeyError:
                char_map[character] = 1
        non_rep = ''
        for key, value in char_map.items():
            if value == 1:
                non_rep = key
                break

        for char_idx in range(len(s)):
            if s[char_idx] == non_rep:
                return char_idx

        return -1
        