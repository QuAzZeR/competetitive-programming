from typing import List
import unittest


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = ["0"]
        def invert(v):
            m  = {
                "0": "1",
                "1": "0"
            }
            return ''.join([m[i] for i in v])
        for i in range(1,n):
            s.append(s[i-1] + "1" + invert(s[i-1])[::-1])

        return s[-1][k-1]



class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.findKthBit(3,1), "0")
        self.assertEqual(s.findKthBit(4,11), "1")


if __name__ == "__main__":
    unittest.main()
