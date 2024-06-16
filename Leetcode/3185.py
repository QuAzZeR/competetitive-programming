from typing import List
from collections import Counter, defaultdict


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        answer = 0
        d = [0] * 24
        n = len(hours)
        for i in range(n):
            answer += d[(24 - hours[i] % 24) % 24]
            d[hours[i] % 24] += 1
        n = len(hours)
        return answer


print(Solution().countCompleteDayPairs([12, 12, 30, 24, 24]))
print(Solution().countCompleteDayPairs([72, 48, 24, 3]))
