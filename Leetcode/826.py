from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        answer = 0

        n = len(difficulty)
        w = len(worker)
        m = max(difficulty)
        d = [0] * (m + 1)
        for i in range(n):
            d[difficulty[i]] = max(d[difficulty[i]], profit[i])
        for i in range(1, m + 1):
            d[i] = max(d[i], d[i - 1])
        for i in range(w):
            if worker[i] > m:
                answer += d[m]
            else:
                answer += d[worker[i]]
        return answer


print(
    Solution().maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7])
)
print(Solution().maxProfitAssignment([85, 47, 57], [24, 66, 99], [40, 25, 25]))
