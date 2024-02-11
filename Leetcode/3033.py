from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        max_column = []
        m = len(matrix)
        n = len(matrix[0])
        for j in range(n):
            x = []
            for i in range(m):
                x.append(matrix[i][j])
            max_column.append(max(x))
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = max_column[j]
        return matrix


print(Solution().modifiedMatrix([[1, 2, -1], [4, -1, 6], [7, 8, 9]]))
print(Solution().modifiedMatrix([[3, -1], [5, 2]]))
