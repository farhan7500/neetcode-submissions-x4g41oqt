class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_list = [0] * 26
        for character in s:
            count_list[ord(character) - ord('a')] += 1

        for character in t:
            count_list[ord(character) - ord('a')] -= 1

        for num in count_list:
            if num != 0:
                return False

        return True

        