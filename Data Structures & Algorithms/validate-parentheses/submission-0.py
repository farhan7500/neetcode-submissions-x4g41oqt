class Solution:
    def isValid(self, s: str) -> bool:
        open_list = ['(', '{', '[']
        close_list = [')', '}', ']']
        if s[0] in close_list:
            return False
        if s[-1] in open_list:
            return False
        if len(s) % 2 == 1:
            return False
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if stack.pop() != '(':
                    return False
            if i == '[':
                stack.append(i)
            elif i == ']':
                if stack.pop() != '[':
                    return False
            if i == '{':
                stack.append(i)
            elif i in '}':
                if stack.pop() != '{':
                    return False
        if len(stack) > 0:
            return False

        return True