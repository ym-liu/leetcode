class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                # populate result
                j, _ = stack.pop()
                result[j] = i - j

            stack.append((i, temp))  # we guarantee that stack is monotonic

        return result
