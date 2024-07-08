import unittest


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        answer = 0
        for i in range(1, n + 1):
            answer = (answer + k) % i
        return answer + 1


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.findTheWinner(5, 2), 3)
        self.assertEqual(s.findTheWinner(6, 5), 1)


if __name__ == "__main__":
    unittest.main()
