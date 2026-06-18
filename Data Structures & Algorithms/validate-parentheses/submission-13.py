class Solution:
    def isValid(self, s: str) -> bool:
        openers = {
            '}': '{',
            ')': '(',
            ']': '[',
        }

        stack = []

        for c in s:
            if c not in openers:
                stack.append(c)
            elif not stack or stack.pop() != openers[c]:
                return False
        return len(stack) == 0
