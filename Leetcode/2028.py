from typing import List
import unittest


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        answer = []
        m = len(rolls)
        s = mean*(m+n)
        diff = s - sum(rolls)
        d = diff // n
        if diff < n or d > 6:
            return answer
        if diff %n == 0:
            return [d] * n
        v = diff - d * n
        if d == 6 and v >= 1:
            return []
        answer = [d] *(n-v) + [d+1] * v


        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.missingRolls([3,2,4,3], 4, 2), [6,6])
        self.assertEqual(s.missingRolls([1,5,6], 3, 4), [2,3,2,2])
        self.assertEqual(s.missingRolls([1,2,3,4], 6, 4), [])
        self.assertEqual(s.missingRolls([6,3,4,3,5,3],1,6), [])


if __name__ == "__main__":
    unittest.main()
