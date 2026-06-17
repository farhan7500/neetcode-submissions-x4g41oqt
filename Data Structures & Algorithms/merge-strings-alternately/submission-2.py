class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_1 = len(word1)
        len_2 = len(word2)

        size_to_loop = min(len_1, len_2)

        result = []
        for i in range(size_to_loop):
            result.append(word1[i])
            result.append(word2[i])

        if len_1 > len_2:
            result.extend(list(word1[size_to_loop:]))
        if len_2 > len_1:
            result.extend(list(word2[size_to_loop:]))

        return ''.join(result)
