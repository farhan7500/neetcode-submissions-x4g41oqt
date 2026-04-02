from string import ascii_lowercase

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dict for grouping the strings against the tuple
        tuple_dict = {}
        # For each string, get the tuple
        for word in strs:
            string_tuple = self.get_string_tuple(word)
            # Add the string against the tuple to the dict
            if tuple_dict.get(string_tuple) is None:
                tuple_dict[string_tuple] = [word]
            else:
                tuple_dict[string_tuple].append(word)
        # Add the dict values to the result list
        result_list = []
        for value in tuple_dict.values():
            result_list.append(value)
        return result_list

    def get_string_tuple(self, word):
        result_tuple = [0] * 26
        for character in word:
            result_tuple[ord(character) - 97] += 1
        return tuple(result_tuple)

            
        