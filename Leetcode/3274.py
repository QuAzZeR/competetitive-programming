import unittest


class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        c1 = (ord(coordinate1[0])-97)%2
        c2 = (ord(coordinate2[0])-97)%2
        if c1 == c2:
            return int(coordinate2[1])%2 == int(coordinate1[1]) %2
        else:
            return int(coordinate2[1])%2 != int(coordinate1[1]) %2


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.checkTwoChessboards("a1", "c3"), True)
        self.assertEqual(s.checkTwoChessboards("a1", "h3"), False)


if __name__ == "__main__":
    unittest.main()
