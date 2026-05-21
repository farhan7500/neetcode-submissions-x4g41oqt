class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq_map = self.get_freq_map(s1)
        i = 0
        j = len(s1)
        while j <= len(s2):
            if self.get_freq_map(s2[i:j]) == s1_freq_map:
                return True
            i += 1
            j += 1

        return False

    def get_freq_map(self, pattern):
        freq_map = {}
        for character in pattern:
            freq_map[character] = freq_map.get(character, 0) + 1
        return freq_map



