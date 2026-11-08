class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']

        stack = []
        result = 0
        for token in tokens:
            if token not in operators:
                token = int(token)
                stack.append(token)
            else:
                if token == '+':
                    result = stack.pop() + stack.pop()
                elif token == '-':
                    result = 0 - stack.pop() + stack.pop()
                elif token == '*':
                    result = stack.pop() * stack.pop()
                else:
                    result = (1 / stack.pop()) * stack.pop()
                stack.append(int(result))
        return stack[0]

        