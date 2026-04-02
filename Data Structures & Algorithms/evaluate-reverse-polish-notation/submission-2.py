class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                int(token)
                stack.append(int(token))
            except ValueError:
                if token == '+':
                    result = stack.pop() + stack.pop()
                    stack.append(result)
                elif token == '-':
                    result = 0 - stack.pop() + stack.pop()
                    stack.append(result)
                elif token == '*':
                    result = stack.pop() * stack.pop()
                    stack.append(result)
                else:
                    result = int(1 / stack.pop() * stack.pop())
                    stack.append(result)

        return stack[0]
