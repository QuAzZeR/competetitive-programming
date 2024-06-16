from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        answer = 0
        n = len(hours)
        for i in range(n):
            for j in range(i + 1, n):
                if (hours[i] + hours[j]) % 24 == 0:
                    answer += 1
        return answer


print(Solution().countCompleteDayPairs([12, 12, 30, 24, 24]))
print(Solution().countCompleteDayPairs([72, 48, 24, 3]))
