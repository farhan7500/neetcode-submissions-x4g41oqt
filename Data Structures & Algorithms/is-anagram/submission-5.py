class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.get_character_list(s) == self.get_character_list(t)
        
    def get_character_list(self, word):
        charater_list = [0] * 26
        for character in word:
            char_num = ord(character) - ord('a')
            charater_list[char_num] += 1
        return charater_list

