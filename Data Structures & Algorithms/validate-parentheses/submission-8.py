class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '[', '{']

        stack = []

        for c in s:
            if c in opening:
                stack.append(c)
            if c == ')' and not (stack and stack.pop() == '('):
                return False
            elif c == '}' and not (stack and stack.pop() == '{'):
                return False
            elif c == ']' and not (stack and stack.pop() == '['):
                return False

        if stack:
            return False

        return True