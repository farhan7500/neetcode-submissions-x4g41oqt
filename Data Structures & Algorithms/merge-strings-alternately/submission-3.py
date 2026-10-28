class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        min_length = min(len(word1), len(word2))

        for index in range(min_length):
            result += word1[index]
            result += word2[index]

        if len(word1) > len(word2):
            result += word1[min_length:]
        else:
            result += word2[min_length:]

        return result
        