from typing import List
class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)


    def adjacentSum(self, value: int) -> int:
        answer = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == value:
                    if i-1 >= 0:
                        answer += self.grid[i-1][j]
                    if i+1 < self.n:
                        answer += self.grid[i+1][j]
                    if j-1 >= 0:
                        answer += self.grid[i][j-1]
                    if j+1 < self.n:
                        answer += self.grid[i][j+1]
                    return answer


    def diagonalSum(self, value: int) -> int:
        answer = 0

        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == value:
                    if i-1 >= 0:
                        if j-1 >= 0:
                            answer += self.grid[i-1][j-1]
                        if j+1 < self.n:
                            answer += self.grid[i-1][j+1]
                        answer += self.grid[i-1][j]
                    if i+1 < self.n:
                        if j-1 >= 0:
                            answer += self.grid[i+1][j-1]
                        if j+1 < self.n:
                            answer += self.grid[i+1][j+1]
                    return answer



# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
