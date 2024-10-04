from typing import List
import unittest


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        m = skill[0] + skill[-1]
        s = 0
        n = len(skill)
        for i in range(n //2):
            if skill[i] + skill[n - i-1] != m:
                return -1
            s += skill[i] * skill[n-i-1]

        return s


class TestCase(unittest.TestCase):
    def test_example(self):
        s = Solution()
        self.assertEqual(s.dividePlayers([3,2,5,1,3,4]), 22)
        self.assertEqual(s.dividePlayers([3,4]), 12)
        self.assertEqual(s.dividePlayers([1,1,2,3]), -1)


if __name__ == "__main__":
    unittest.main()
