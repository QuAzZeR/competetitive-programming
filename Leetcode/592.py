from typing import List
import re
import unittest
from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
        numerator = 0
        denominator = 1
        for i in range(0, len(nums), 2):
            n, den = nums[i],nums[i + 1]
            numerator = numerator * den + n * denominator
            denominator *= den
        c = gcd(numerator, denominator)
        return  f"{numerator // c}/{denominator//c}"


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.fractionAddition("-1/2+1/2"), "0/1")
        self.assertEqual(s.fractionAddition("-1/2+1/2+1/3"), "1/3")
        self.assertEqual(s.fractionAddition("1/3-1/2"), "-1/6")


if __name__ == "__main__":
    unittest.main()
