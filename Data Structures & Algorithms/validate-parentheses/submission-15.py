class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        stack = []

        opening = ['[', '{', '(']

        if s[0] not in opening:
            return False
        if s[-1] in opening:
            return False

        for c in s:
            if c in opening:
                stack.append(c)
            elif c == ']' and not (stack and stack.pop() == '['):
                return False
            elif c == '}' and not (stack and stack.pop() == '{'):
                return False
            elif c == ')' and not (stack and stack.pop() == '('):
                return False
        
        if len(stack) != 0:
            return False
        return True