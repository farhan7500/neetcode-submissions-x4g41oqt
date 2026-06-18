class Solution:
    def isValid(self, s: str) -> bool:
        openers = [
            '{',
            '(',
            '[',
        ]

        stack = []

        for c in s:
            if c in openers:
                stack.append(c)
            elif c == '}' and (stack and stack.pop()) != '{':
                return False
            elif c == ']' and (stack and stack.pop()) != '[':
                return False
            elif c == ')' and (stack and stack.pop()) != '(':
                return False
        return len(stack) == 0