from typing import List
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        answer = [[0]* n for _ in range(m)]

        for j in range(n):
            i = 0
            ii = i
            jj = j
            c = []
            while ii < m and jj < n:
                c.append(mat[ii][jj])
                ii += 1
                jj += 1
            c = sorted(c)
            index = 0
            ii = i
            jj = j
            while ii < m and jj < n:
                mat[ii][jj] = c[index]
                ii += 1
                jj += 1
                index+=1
        for i in range(m):
            j = 0
            ii = i
            jj = j
            c = []
            while ii < m and jj < n:
                c.append(mat[ii][jj])
                ii += 1
                jj += 1
            c = sorted(c)
            index = 0
            ii = i
            jj = j
            while ii < m and jj < n:
                mat[ii][jj] = c[index]
                ii += 1
                jj += 1
                index += 1
        return mat
print(Solution().diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
print(Solution().diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]))
