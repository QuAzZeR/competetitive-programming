from typing import List
import unittest


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(4*n*n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)
        for i in range(n):
            for j in range(n):
                r = 4 * (i*n+j)
                v = grid[i][j]
                if v in '/ ':
                    union(r + 0, r + 3)
                    union(r + 1, r + 2)
                if v in '\\ ':
                    union(r + 0, r + 1)
                    union(r + 2, r + 3)
                if j + 1 < n:
                    union(r + 1, r + 7)
                if i + 1 < n:
                    union(r + 2, r + 4 * n)
        return sum(find(x) == x  for x in range(4 * n * n))


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.regionsBySlashes( [" /","/ "]), 2)
        self.assertEqual(s.regionsBySlashes([" /","  "]), 1)
        self.assertEqual(s.regionsBySlashes(["/\\","\\/"]), 5)


if __name__ == "__main__":
    unittest.main()
