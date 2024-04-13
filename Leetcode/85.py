from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        answer = 0
        rows = len(matrix)
        cols = len(matrix[0])
        d = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            d[i][0] = 1 if matrix[i][0] == "1" else 0

        for i in range(rows):
            for j in range(1, cols):
                if matrix[i][j] == "1":
                    if d[i][j - 1]:
                        d[i][j] = d[i][j - 1] + 1
                    else:
                        d[i][j] = 1

        for j in range(cols):
            c = []
            for i in range(rows):
                c.append(d[i][j])

            for i in range(len(c)):
                left = i
                right = i
                value = c[i]
                count = 1
                while left >= 0 and c[left] >= value:
                    if left != i:
                        count += 1
                    left -= 1
                while right < len(c) and c[right] >= value:
                    if right != i:
                        count += 1
                    right += 1
                answer = max(answer, value * count)
        return answer


print(
    Solution().maximalRectangle(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )
)
