class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                if token == '+':
                    stack.append(stack.pop() + stack.pop())
                elif token == '-':
                    second = 0 - stack.pop()
                    stack.append(stack.pop() + second)
                elif token == '*':
                    stack.append(stack.pop() * stack.pop())
                else:
                    stack.append(int(1 / stack.pop() * stack.pop()))
        return stack[0]
        