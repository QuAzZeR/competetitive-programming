from typing import List
import unittest


class Solution:
    def getSmallestString(self, s: str) -> str:
        n = len(s)
        answer = s
        for i in range(1, n):
            if int(s[i]) % 2 == int(s[i - 1]) % 2:
                t = list(s)
                temp = t[i]
                t[i] = t[i - 1]
                t[i - 1] = temp
                answer = min(answer, "".join(t))

        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.getSmallestString("45320"), "43520")
        self.assertEqual(s.getSmallestString("001"), "001")


if __name__ == "__main__":
    unittest.main()
