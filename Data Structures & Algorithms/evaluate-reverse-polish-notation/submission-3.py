class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                int(token)
                stack.append(int(token))
            except ValueError:
                if token == '+':
                    stack.append(stack.pop() + stack.pop())
                elif token == '-':
                    stack.append(0 - stack.pop() + stack.pop())
                elif token == '*':
                    stack.append(stack.pop() * stack.pop())
                else:
                    stack.append(int(1 / stack.pop() * stack.pop()))

        return stack[0]
