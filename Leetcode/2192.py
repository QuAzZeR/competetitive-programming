from typing import List
import unittest


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        self.answer = [[] for _ in range(n)]
        self.parents = [[] for _ in range(n)]

        def dfs(p, c, visited):
            visited[c] = True
            for d in self.parents[c]:
                if not visited[d]:
                    self.answer[d].append(p)
                    dfs(p, d, visited)

        for edge in edges:
            self.parents[edge[0]].append(edge[1])
        for i in range(n):
            dfs(i, i, [False] * n)
        for i in range(n):
            self.answer[i].sort()
        return self.answer


class Testcase(unittest.TestCase):
    def test(self):
        n = 8
        edge_list = [
            [0, 3],
            [0, 4],
            [1, 3],
            [2, 4],
            [2, 7],
            [3, 5],
            [3, 6],
            [3, 7],
            [4, 6],
        ]
        expected_output = [
            [],
            [],
            [],
            [0, 1],
            [0, 2],
            [0, 1, 3],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3],
        ]
        s = Solution()
        self.assertListEqual(s.getAncestors(n, edge_list), expected_output)
        n = 5
        edge_list = [
            [0, 1],
            [0, 2],
            [0, 3],
            [0, 4],
            [1, 2],
            [1, 3],
            [1, 4],
            [2, 3],
            [2, 4],
            [3, 4],
        ]
        expected_output = [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
        self.assertListEqual(s.getAncestors(n, edge_list), expected_output)


if __name__ == "__main__":
    unittest.main()
