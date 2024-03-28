from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles = sorted(piles, reverse=True)
        answer = 0
        for i in range(n):
            answer += piles[2 * i + 1]
        return answer


print(Solution().maxCoins([2, 4, 1, 2, 7, 8]))
print(Solution().maxCoins([2, 4, 5]))
print(Solution().maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]))
