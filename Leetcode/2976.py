from typing import List
import unittest


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = 26
        a = [[float('inf')] * n for _ in range(n)]
        for i in range(len(original)):
            v1 = ord(original[i]) - 97
            v2 = ord(changed[i]) - 97
            a[v1][v2] = min(a[v1][v2], cost[i])

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    a[j][k] = min(a[j][k], a[j][i] + a[i][k])
        answer = 0
        for i in range(len(source)):
            v1 = ord(source[i]) - 97
            v2 = ord(target[i]) - 97

            if v1 == v2:
                continue
            if a[v1][v2] == float('inf'):
                return -1
            answer += a[v1][v2]
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]), 28)
        self.assertEqual(s.minimumCost(source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]), 12)
        self.assertEqual(s.minimumCost(source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]), -1)


if __name__ == "__main__":
    unittest.main()
