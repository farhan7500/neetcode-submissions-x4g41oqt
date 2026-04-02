class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1

        # character_map = {}
        # for character in s:
        #     try:
        #         character_map[character] += 1
        #     except KeyError:
        #         character_map[character] = 1
        # for character in t:
        #     try:
        #         character_map[character] -= 1
        #     except KeyError:
        #         return False
        # for v in character_map.values():
        #     if v != 0:
        #         return False
        # return True

        # Solution 2
        letter_occurances = [0] * 26
        for character in s:
            char_num = ord(character) - ord('a')
            letter_occurances[char_num] += 1

        for character in t:
            char_num = ord(character) - ord('a')
            letter_occurances[char_num] -= 1
            if letter_occurances[char_num] < 0:
                return False
        
        for letter in letter_occurances:
            if letter != 0:
                return False
        return True





        