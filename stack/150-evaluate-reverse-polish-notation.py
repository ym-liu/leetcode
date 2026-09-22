class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            num = self.isInt(token)
            if num is not None:
                stack.append(num)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self.doOperation(operand1, operand2, token)
                stack.append(result)

        return stack[0]

    def isInt(self, s: str) -> int | None:
        try:
            return int(s)

        except ValueError:
            return None

    def doOperation(self, operand1: int, operand2: int, operation: str) -> int:
        if operation == "+":
            return operand1 + operand2
        elif operation == "-":
            return operand1 - operand2
        elif operation == "*":
            return operand1 * operand2
        elif operation == "/":
            return int(operand1 / operand2)
        else:
            return "wtf"
