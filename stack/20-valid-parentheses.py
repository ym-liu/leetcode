class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if not stack:
                    return False

                bracket = stack.pop()
                if not self.isComplement(bracket, c):
                    return False

        return not stack

    def isComplement(self, open_bracket: str, close_bracket: str) -> bool:
        return (
            (open_bracket == "(" and close_bracket == ")")
            or (open_bracket == "[" and close_bracket == "]")
            or (open_bracket == "{" and close_bracket == "}")
        )
