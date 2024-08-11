from typing import List
import unittest


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def count_islands():
            seen = set()
            def dfs(r,c):
                stack = [(r,c)]
                while stack:
                    x,y = stack.pop()
                    for nx,ny in [(x-1,y), (x+1,y), (x, y-1), (x,y+1)]:
                        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] and (nx,ny) not in seen:
                            seen.add((nx,ny))
                            stack.append((nx,ny))

            islands = 0
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1 and (i,j) not in seen:
                        islands += 1
                        seen.add((i,j))
                        dfs(i,j)
            return islands


        if count_islands() != 1:
            return 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1
        return 2

class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minDays([[0,1,1,0],[0,1,1,0],[0,0,0,0]]), 2)
        self.assertEqual(s.minDays([[1,1]]), 2)


if __name__ == "__main__":
    unittest.main()
