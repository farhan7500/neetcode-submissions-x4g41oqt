class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        while right < len(s2):
            if self.is_anagram(s1, s2[left: right + 1]):
                return True
            left += 1
            right += 1
        return False

    def is_anagram(self, p1, p2):
        count_map = {}
        for c in p1:
            try:
                count_map[c] += 1
            except KeyError:
                count_map[c] = 1

        for c in p2:
            try:
                if count_map[c] == 0:
                    return False
                count_map[c] -= 1
            except KeyError:
                return False

        for v in count_map.values():
            if v != 0:
                return False

        return True
