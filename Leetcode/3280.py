from typing import List
import unittest


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join([bin(int(i)).split('b')[-1] for i in date.split("-")])


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.convertDateToBinary("2080-02-29"), "100000100000-10-11101")
        self.assertEqual(s.convertDateToBinary("1900-01-01"), "11101101100-1-1")


if __name__ == "__main__":
    unittest.main()
