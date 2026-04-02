class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            char_tuple = self.get_char_tuple(s)
            if(char_tuple in anagram_map):
                anagram_map[char_tuple].append(s)
            else:
                anagram_map[char_tuple] = [s]
        return list(anagram_map.values())


    def get_char_tuple(self, element):
        result_list = [0] * 26
        for character in element:
            result_list[ord(character) - ord('a')] += 1
        return tuple(result_list)
