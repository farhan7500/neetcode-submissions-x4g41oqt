class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        character_map = {}

        for c in s:
            try:
                character_map[c] += 1
            except KeyError:
                character_map[c] = 1

        for c in t:
            try:
                if character_map[c] == 0:
                    return False
                character_map[c] -= 1
            except KeyError:
                return False

        for value in character_map.values():
            if value != 0:
                return False
        return True
