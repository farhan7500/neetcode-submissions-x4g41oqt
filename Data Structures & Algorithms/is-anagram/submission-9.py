class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        count_list = [0] * 26
        for c in s:
            count_list[ord(c) - ord('a')] += 1
        for c in t:
            count_list[ord(c) - ord('a')] -= 1
        for el in count_list:
            if el != 0:
                return False
        return True
        