from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        l = 1
        r = max(bloomDay)

        def bns(d):
            bonquets = 0
            f = 0
            for b in bloomDay:
                if b > d:
                    f = 0
                else:
                    bonquets += (f + 1) // k
                    f = (f + 1) % k
            return bonquets >= m

        while l < r:
            mid = l + (r - l) // 2
            if bns(mid):
                r = mid
            else:
                l = mid + 1

        return l


print(Solution().minDays([1, 10, 3, 10, 2], 3, 1))
print(Solution().minDays([1, 10, 3, 10, 2], 3, 2))
print(Solution().minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))
