class Solution:
    def isValid(self, s: str) -> bool:
        pars = {"}":"{",
                ")":"(",
                "]":"["}

        stack = []

        for i in s :
            if i not in pars :
                stack.append(i)
            elif stack and pars[i] == stack[-1] :
                stack.pop()
            else :
                return False
        return stack == []
