import unittest


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h, m = [int(i) for i in current.split(":")]
        eh, em = [int(i) for i in correct.split(":")]
        self.answer = -1
        d = (eh * 60 + em) - (h * 60 + m)
        return d // 60 + (d % 60 // 15) + (d % 15 // 5) + (d % 5)


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.convertTime("02:30", "04:35"), 3)
        self.assertEqual(s.convertTime("11:00", "11:01"), 1)


if __name__ == "__main__":
    unittest.main()
