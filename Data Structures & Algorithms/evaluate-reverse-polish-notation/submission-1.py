class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens :

            if char not in "+-/*" :
                stack.append(int(char))

            else :
                op2 = stack.pop()
                op1 = stack.pop()
                val = 0
                if char == "+" :
                    val = op1 + op2
                elif char == "-" :
                    val = op1 - op2
                elif char == "*" :
                    val = op1 * op2
                else :
                    val = int(op1 / op2)

                stack.append(val)

        return stack.pop()
