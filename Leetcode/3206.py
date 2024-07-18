from typing import List
import unittest


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        answer = 0
        n = len(colors)
        if colors[-1] != colors[0] and colors[0] != colors[1]:
            answer += 1
        if colors[-1] != colors[0] and colors[-1] != colors[-2]:
            answer += 1
        for i in range(1, n - 1):
            if colors[i] != colors[i - 1] and colors[i] != colors[i + 1]:
                answer += 1

        return answer


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.numberOfAlternatingGroups([1, 1, 1]), 0)
        self.assertEqual(s.numberOfAlternatingGroups([0, 1, 0, 0, 1]), 3)


if __name__ == "__main__":
    unittest.main()
