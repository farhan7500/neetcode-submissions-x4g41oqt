class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        starters = ['(', '[', '{']
        for character in s:
            if character in starters:
                stack.append(character)
            else:
                if character == ')' and (stack and stack.pop()) != '(':
                    return False
                if character == ']' and (stack and stack.pop()) != '[':
                    return False
                if character == '}' and (stack and stack.pop()) != '{':
                    return False

        if len(stack) > 0:
            return False

        return True
