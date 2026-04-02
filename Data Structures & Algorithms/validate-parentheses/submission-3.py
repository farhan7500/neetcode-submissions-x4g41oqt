class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_list = ['(', '{', '[']
        close_list = [')', '}', ']']
        if s[0] in close_list:
            return False
        if s[-1] in open_list:
            return False
        if len(s) % 2 == 1:
            return False
        
        for character in s:
            if character in open_list:
                stack.append(character)
            else:
                if character == '}' and stack.pop() != '{':
                    return False
                if character == ']' and stack.pop() != '[':
                    return False
                if character == ')' and stack.pop() != '(':
                    return False
        if stack:
            return False
        return True


        