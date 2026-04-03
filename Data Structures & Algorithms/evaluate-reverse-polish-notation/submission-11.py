class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif token == '-':
                stack.append(0 - int(stack.pop()) + int(stack.pop()))
            elif token == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif token == '/':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                stack.append(float(val2) / val1)
            else:
                stack.append(int(token))
        return int(stack[0])
        