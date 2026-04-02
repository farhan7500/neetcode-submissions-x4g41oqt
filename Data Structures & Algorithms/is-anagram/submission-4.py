class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        element_dict = {}
        for el in s:
            try:
                element_dict[el] += 1
            except KeyError:
                element_dict[el] = 1
        for el in t:
            try:
                if element_dict[el] == 0:
                    return False
                element_dict[el] -= 1
            except KeyError:
                return False

        for v in element_dict.values():
            if v != 0:
                return False
        return True

        