from typing import List
import unittest


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        s = sorted([str(i) for i in nums],reverse=True, key=lambda x: x*10)
        if s[0] == "0":
            return "0"

        return ''.join(s)


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.largestNumber([10, 2]), "210")
        self.assertEqual(s.largestNumber([3,30,34,5,9]), "9534330")


if __name__ == "__main__":
    unittest.main()
