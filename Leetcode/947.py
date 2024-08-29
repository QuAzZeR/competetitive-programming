from typing import List
import unittest


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        self.visited = [False] * n
        groups = 0
        def dfs(i):
            self.visited[i] = True
            for j in range(n):
                if not self.visited[j]:
                    if stones[i][0] == stones[j][0]:
                        dfs(j)
                    if stones[i][1] == stones[j][1]:
                        dfs(j)


        for i in range(n):
            if not self.visited[i]:
                groups += 1
                dfs(i)
        return n -groups


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]), 5)
        self.assertEqual(s.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]), 3)


if __name__ == "__main__":
    unittest.main()
