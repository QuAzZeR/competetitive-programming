import unittest


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        answer = 0
        factor = 2
        while n > 1:
            while n%factor == 0:
                answer += factor
                n //= factor
            factor += 1

        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.minSteps(3), 3)
        self.assertEqual(s.minSteps(1), 0)


if __name__ == "__main__":
    unittest.main()
