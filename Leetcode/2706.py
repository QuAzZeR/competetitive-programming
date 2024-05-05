from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        n = len(prices)
        answer = 100 * 2
        for i in range(n):
            for j in range(i + 1, n):
                if money - (prices[i] + prices[j]) >= 0:
                    answer = min(answer, prices[i] + prices[j])
        if answer == 200:
            return money
        return money - answer


print(Solution().buyChoco([1, 2, 2], 3))
print(Solution().buyChoco([3, 2, 3], 3))
print(Solution().buyChoco([98, 54, 6, 34, 66, 63, 52, 39], 62))
