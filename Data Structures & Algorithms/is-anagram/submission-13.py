class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1
        char_count_map = {}
        for c in s:
            try:
                char_count_map[c] += 1
            except KeyError:
                char_count_map[c] = 1
        
        for c in t:
            try:
                if char_count_map[c] == 0:
                    return False
                char_count_map[c] -= 1
            except KeyError:
                return False
        
        for v in char_count_map.values():
            if v != 0:
                return False
        
        return True

        
        