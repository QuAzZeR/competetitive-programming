from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        answer = duration
        n = len(timeSeries)
        for i in range(n - 1):
            c = timeSeries[i]
            n = timeSeries[i + 1]
            if c + duration - 1 < n:
                answer += duration
            else:
                answer += n - 1
        return answer


print(Solution().findPoisonedDuration([1, 4], 2))
print(Solution().findPoisonedDuration([1, 2], 2))
