class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []  # Current parentheses string we're building
        res = []    # Store all valid combinations

        def backtrack(openN, closedN):
            # We have used all n opening and n closing parentheses,
            # so the current stack is a complete valid combination.
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # We can add another "(" as long as we haven't used all n.
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)  # Explore this choice
                stack.pop()                    # Undo the choice

            # We can add ")" only if there is an unmatched "(".
            # closedN < openN means there is currently an open
            # parenthesis that still needs to be closed.
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)  # Explore this choice
                stack.pop()                    # Undo the choice

        backtrack(0, 0)  # Start with 0 "(" and 0 ")"
        return res