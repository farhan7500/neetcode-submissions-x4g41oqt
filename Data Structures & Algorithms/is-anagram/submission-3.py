class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        element_count_map = {}
        for el in s:
            try:
                element_count_map[el] += 1
            except KeyError:
                element_count_map[el] = 1

        for el in t:
            try:
                if element_count_map[el] == 0:
                    return False
                element_count_map[el] -= 1
            except KeyError:
                return False

        for v in element_count_map.values():
            if v != 0:
                return False

        return True
