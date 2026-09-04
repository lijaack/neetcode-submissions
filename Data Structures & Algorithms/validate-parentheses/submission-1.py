class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}":"{", ")":"(","]":"["}
        stack = []
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(c)
        return True if not stack else False
