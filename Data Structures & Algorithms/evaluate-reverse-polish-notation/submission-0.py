class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(first + second)

            elif token == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)

            elif token == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(first * second)

            elif token == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))

            else:
                stack.append(int(token))

        return stack[0]