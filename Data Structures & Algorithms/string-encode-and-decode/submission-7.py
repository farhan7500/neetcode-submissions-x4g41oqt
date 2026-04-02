class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    def decode(self, s: str) -> List[str]:
        pos = 0
        result_list = []
        while pos < len(s):
            num = ''
            while s[pos] != '#':
                num += s[pos]
                pos += 1
            length = int(num)
            result_list.append(s[pos + 1: pos + 1 + length])
            pos = pos + 1 + length
        return result_list
        
