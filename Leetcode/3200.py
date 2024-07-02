import unittest


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def finding(a, b):
            h = 0
            i = 1
            while True:
                if i % 2 == 1:
                    if a >= i:
                        a -= i
                    else:
                        break
                else:
                    if b >= i:
                        b -= i
                    else:
                        break
                h += 1
                i += 1
            return h

        return max(finding(red, blue), finding(blue, red))


class Testcase(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.maxHeightOfTriangle(2, 4), 3)
        self.assertEqual(s.maxHeightOfTriangle(2, 1), 2)
        self.assertEqual(s.maxHeightOfTriangle(1, 1), 1)
        self.assertEqual(s.maxHeightOfTriangle(10, 1), 2)


if __name__ == "__main__":
    unittest.main()
