class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        character_map = {}
        for character in s:
            try:
                character_map[character] += 1
            except KeyError:
                character_map[character] = 1
        for character in t:
            try:
                character_map[character] -= 1
            except KeyError:
                return False
        for v in character_map.values():
            if v != 0:
                return False
        return True

        