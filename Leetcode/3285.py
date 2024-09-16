from typing import List
from collections import Counter
import unittest


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        answer = []
        n = len(height)
        for i in range(1, n):
            if height[i-1] > threshold:
                answer.append(i)
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.stableMountains([1,2,3,4,5], 2), [3,4])
        self.assertEqual(s.stableMountains([10,1,10,1,10], 3), [1,3])
        self.assertEqual(s.stableMountains( [10,1,10,1,10], 10), [])


if __name__ == "__main__":
    unittest.main()
