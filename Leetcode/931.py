from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        self.n = len(matrix)
        self.m = matrix
        if self.n == 1:
            return matrix[0][0]
        self.dp = [[100*self.n]*self.n for _ in range(self.n)]
        answer = 100*self.n
        for i in  range(self.n):
            answer = min(answer,self.walk(0, i))
        return answer
    def walk(self, row, column):
        left = right = 100*self.n
        if self.dp[row][column] != 100*self.n:
            return self.dp[row][column]

        if row == self.n-1:
            return self.m[row][column]

        if column -1 >=0:
            left = self.walk(row+1, column-1)

        straight = self.walk(row+1, column)

        if column + 1 < self.n:
            right = self.walk(row+1, column+1)

        self.dp[row][column] = min([left,straight, right]) + self.m[row][column]

        return self.dp[row][column]

print(Solution().minFallingPathSum([[2,1,3], [6,5,4], [7,8,9]]))
print(Solution().minFallingPathSum([[-19,57], [-40,-5]]))
print(Solution().minFallingPathSum([[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]))
