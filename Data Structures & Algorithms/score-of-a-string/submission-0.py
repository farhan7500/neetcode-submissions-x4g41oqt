class Solution:
    def scoreOfString(self, s: str) -> int:
        last_character = None
        total = 0
        for character in s:
            if last_character is not None:
                total += abs(ord(character) - last_character)
                last_character = ord(character)
            else:
                last_character = ord(character)

        return total



        