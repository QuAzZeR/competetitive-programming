from typing import List
import unittest


class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        pp = self.find(p)
        qq = self.find(q)
        if pp == qq:
            return False
        self.count -= 1
        if self.rank[pp] > self.rank[qq]:
            pp, qq = qq, pp
        self.parent[pp] = qq
        self.rank[qq] += self.rank[pp]
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ua = UnionFind(n)
        ub = UnionFind(n)
        answer = 0
        edges.sort(reverse=True)
        for edge in edges:
            t, u, v = edge
            u = u - 1
            v = v - 1
            if t == 3:
                answer += not (ua.union(u, v) and ub.union(u, v))
            elif t == 2:
                answer += not ub.union(u, v)  # Bob only
            else:
                answer += not ua.union(u, v)
        return answer if ua.count == 1 and ub.count == 1 else -1


class TestCase(unittest.TestCase):
    def test_example(self):
        n = 4
        edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
        s = Solution()
        self.assertEqual(s.maxNumEdgesToRemove(n, edges), 2)
        n = 4
        edges = [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]
        self.assertEqual(s.maxNumEdgesToRemove(n, edges), 0)

        n = 4
        edges = [[3, 2, 3], [1, 1, 2], [2, 3, 4]]
        self.assertEqual(s.maxNumEdgesToRemove(n, edges), -1)
