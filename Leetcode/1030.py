from typing import List


class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        answer = []
        for i in range(rows):
            for j in range(cols):
                answer.append([abs(i - rCenter) + abs(j - cCenter), [i, j]])
        answer = sorted(answer, key=lambda x: x[0])
        return [i[1] for i in answer]


print(Solution().allCellsDistOrder(1, 2, 0, 0))
print(Solution().allCellsDistOrder(2, 2, 0, 1))
print(Solution().allCellsDistOrder(2, 3, 1, 2))
