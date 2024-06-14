class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # This will store indices of the temperatures list
        res = [0] * len(temperatures)  # Result list initialized to all 0s

        for i, temp in enumerate(temperatures):
            # Pop indices from the stack while the current temperature is           higher than the temperature at those indices
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx  # Calculate the number of days until a warmer temperature
            stack.append(i)  # Push the current index onto the stack

        return res

