class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_1 = len(word1)
        len_2 = len(word2)

        size_to_loop = min(len_1, len_2)

        result = ''
        for i in range(size_to_loop):
            result += word1[i]
            result += word2[i]

        if len_1 > len_2:
            result += word1[size_to_loop:]
        if len_2 > len_1:
            result += word2[size_to_loop:]

        return result
