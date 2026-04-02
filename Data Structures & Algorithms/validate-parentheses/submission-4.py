class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '{', '[']
        stack = []
        for char in s:
            if char in opening:
                stack.append(char)
            if char == ')' and not (len(stack) > 0 and stack.pop() == '('):
                return False
            if char == ']' and not (len(stack) > 0 and stack.pop() == '['):
                return False
            if char == '}' and not (len(stack) > 0 and stack.pop() == '{'):
                return False

        if len(stack) > 0:
            return False
        return True

        