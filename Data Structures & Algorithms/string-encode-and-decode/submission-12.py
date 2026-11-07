class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)) + '#' + s)
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        index = 0
        result = []
        while index < len(s):
            length = ''
            while s[index] != '#':
                length += s[index]
                index += 1
            length = int(length)

            result.append(s[index + 1: index + length + 1])
            index = index + length + 1

        return result
