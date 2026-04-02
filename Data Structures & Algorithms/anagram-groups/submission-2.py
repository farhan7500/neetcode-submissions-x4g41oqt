from string import ascii_lowercase

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        string_map = {}
        
        letter_dict = {v:k for k,v in enumerate(ascii_lowercase)}

        for s in strs:
            initialize_list = [0] * 26
            for c in s:
                initialize_list[letter_dict[c]] += 1
            try:
                string_map[tuple(initialize_list)].append(s)
            except KeyError:
                string_map[tuple(initialize_list)] = [s]

        result_list = []

        for v in string_map.values():
            result_list.append(v)
        return result_list

            
        