class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Iterate through the strs and increment the list index
        # # Create a list with 26 * [0]
        # matching the ASCII(str) - ASCII('a')  

        result_map = {}

        for stri in strs:
            str_occ_list = []
            for i in range(26):
                str_occ_list.append(0)

            for c in stri:
                str_occ_list[ord(c) - ord('a')] += 1

            demilited_str = '#'.join(str(str_occ_list))

            if result_map.get(demilited_str) is not None:
                current_list = result_map[demilited_str]
                current_list.append(stri)
                result_map[demilited_str] = current_list
            else:
                result_map[demilited_str] = [stri]

        return list(result_map.values())