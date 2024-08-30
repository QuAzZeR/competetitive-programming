from typing import List
import unittest


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        answer = []
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.modifiedGraphEdges(5, [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], 0,1,5), [[4,1,1],[2,0,1],[0,3,3],[4,3,1]])
        self.assertEqual(s.modifiedGraphEdges(3, [[0,1,-1],[0,2,5]], 0,2,6),[])


if __name__ == "__main__":
    unittest.main()
