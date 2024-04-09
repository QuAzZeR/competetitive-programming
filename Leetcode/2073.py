from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = 0
        n = len(tickets)
        while tickets[k] != 0:
            for i in range(n):
                if tickets[i] != 0:
                    tickets[i] -= 1
                    t += 1
        return t


print(Solution().timeRequiredToBuy([2, 3, 2], 2))
print(Solution().timeRequiredToBuy([5, 1, 1, 1], 0))
