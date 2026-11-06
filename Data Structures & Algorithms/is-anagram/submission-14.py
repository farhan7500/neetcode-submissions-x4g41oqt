class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1
        # char_count_map = {}
        # for c in s:
        #     try:
        #         char_count_map[c] += 1
        #     except KeyError:
        #         char_count_map[c] = 1
        
        # for c in t:
        #     try:
        #         if char_count_map[c] == 0:
        #             return False
        #         char_count_map[c] -= 1
        #     except KeyError:
        #         return False
        
        # for v in char_count_map.values():
        #     if v != 0:
        #         return False
        
        # return True

        # Solution 2
        # Create a list of 26 0s
        count_list = [0] * 26
        # Add 1 for each index (ord(c) - ord(a)) for string s
        for c in s:
            count_list[ord(c) - ord('a')] += 1
        # Subtract 1 for each index (ord(c) - ord(a)) for string t
        for c in t:
            if count_list[ord(c) - ord('a')] == 0:
                return False
            count_list[ord(c) - ord('a')] -= 1
        # Check if all values are 0
        for el in count_list:
            if el != 0:
                return False
        return True

        
        