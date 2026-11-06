class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # tuple key, list value
        anagram_map = {}

        for s in strs:
            char_count_list = [0] * 26
            for c in s:
                char_count_list[ord(c) - ord('a')] += 1
            char_count_tuple = tuple(char_count_list)
            if anagram_map.get(char_count_tuple) is None:
                anagram_map[char_count_tuple] = [s]
            else:
                anagram_map[char_count_tuple].append(s)

        result = []
        for value in anagram_map.values():
            result.append(value)
        return result
        