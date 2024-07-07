from typing import List
import unittest


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = 0
        empty = 0
        while numBottles != 0:
            answer += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty = empty % numExchange
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.numWaterBottles(9, 3), 13)
        self.assertEqual(s.numWaterBottles(15, 4), 19)


if __name__ == "__main__":
    unittest.main()
