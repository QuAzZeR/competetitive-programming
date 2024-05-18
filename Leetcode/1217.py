from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = 0
        even = 0
        for i in position:
            if i % 2 == 0:
                odd += 1
            else:
                even += 1
        return min(even, odd)


print(Solution().minCostToMoveChips([1, 2, 3]))
print(Solution().minCostToMoveChips([2, 2, 2, 3, 3]))
print(Solution().minCostToMoveChips([1, 1000000000]))
