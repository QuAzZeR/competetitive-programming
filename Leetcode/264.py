from typing import List
import unittest


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1 for i in range(n)]
        p1 = 0
        p2 = 0
        p3 = 0
        for i in range(1, n):
            two = dp[p1] * 2
            three = dp[p2] * 3
            five = dp[p3] * 5
            dp[i] = min([two,three,five])
            if(dp[i] == two):
                p1+=1
            if dp[i] == three:
                p2+=1
            if dp[i] == five:
                p3 += 1
        return dp[-1]


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.nthUglyNumber(10), 12)
        self.assertEqual(s.nthUglyNumber(1), 1)


if __name__ == "__main__":
    unittest.main()
