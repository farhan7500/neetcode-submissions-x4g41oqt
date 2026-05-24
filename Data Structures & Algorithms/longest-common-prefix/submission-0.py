class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        first = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < min(len(first), len(strs[i])):
                if first[j] != strs[i][j]:
                    break
                j += 1
            first = first[:j]
        return first
                






        