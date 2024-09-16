from typing import List
import unittest


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        fh, fm = map(int, timePoints[0].split(':'))
        lh, lm = map(int, timePoints[-1].split(':'))
        answer = (23-lh)*60  + 60 - lm + fh*60 + fm
        n = len(timePoints)
        for i in range(1, n):
            ch, cm = map(int, timePoints[i].split(':'))
            answer = min(answer, (ch - fh) * 60 + (cm - fm))
            fh = ch
            fm = cm
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.findMinDifference(["23:59","00:00"]), 1)
        self.assertEqual(s.findMinDifference(["00:00","23:59","00:00"]), 0)
        self.assertEqual(s.findMinDifference(['12:01', '23:59']), 718)


if __name__ == "__main__":
    unittest.main()
