from collections import defaultdict
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        answer = [0] * l
        stack = []
        for i in range(l - 1, -1, -1):
            current = temperatures[i]
            while len(stack) > 0 and current >= temperatures[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                answer[i] = stack[-1] - i
            stack.append(i)
        return answer


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(Solution().dailyTemperatures([30, 40, 50, 60]))
print(Solution().dailyTemperatures([30, 60, 90]))
