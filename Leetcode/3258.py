from typing import List
import unittest


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        answer = 0
        l = 0
        r = 0
        one = 0
        zero = 0
        n = len(s)
        while r < n:
            if s[r] == '0':
                zero += 1
            else:
                one += 1
            while zero > k and one > k:
                if s[l] == '0':
                    zero -= 1
                else:
                    one -= 1
                l += 1

            answer += (r - l) +1
            r += 1
        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.countKConstraintSubstrings("10101", 1), 12)
        self.assertEqual(s.countKConstraintSubstrings("1010101", 2), 25)
        self.assertEqual(s.countKConstraintSubstrings("11111", 1), 15)


if __name__ == "__main__":
    unittest.main()
