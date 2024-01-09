from typing import List
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat)
        s = 0
        for i in range(l):
            s += mat[i][i]
            if i != l-i-1:
                s += mat[i][l-i-1]

        return s

print(Solution().diagonalSum([[1,2,3],
              [4,5,6],
              [7,8,9]]))
print(Solution().diagonalSum([[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))
print(Solution().diagonalSum([[5]]))
