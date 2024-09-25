from typing import List
import unittest


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        ss = set(dictionary)
        n = len(s)
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            dp[i] = dp[i+1] + 1
            for j in range(1, n-i + 1):
                if s[i:i+j] in ss:
                    dp[i] = min(dp[i], dp[i+j])
        return dp[0]


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minExtraChar("leetscode", ["leet", "code", "leetcode"]), 1)
        self.assertEqual(s.minExtraChar("sayhelloworld", ["hello", "world"]), 3)


if __name__ == "__main__":
    unittest.main()
