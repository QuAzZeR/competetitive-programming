from typing import List
import unittest


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        self.is_sub_island= True
        island = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid2[r][c] == 0:
                return True
            grid2[r][c] = 0
            if grid1[r][c] == 0:
                self.is_sub_island = False
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return self.is_sub_island
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    self.is_sub_island = True
                    if dfs(i,j):
                        island += 1


        return island


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.countSubIslands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]), 3)
        self.assertEqual(s.countSubIslands([[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]), 2)


if __name__ == "__main__":
    unittest.main()
