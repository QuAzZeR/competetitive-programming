from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        n = len(customers)
        answer = 0
        s = 0
        m = 0
        for i in range(n):
            if grumpy[i] == 0:
                answer += customers[i]
            elif i < minutes:
                s += customers[i]
        m = s
        for i in range(minutes, n):
            s += customers[i] * grumpy[i]
            s -= customers[i - minutes] * grumpy[i - minutes]
            m = max(m, s)
        return answer + m


print(Solution().maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
print(Solution().maxSatisfied([1], [0], 1))
